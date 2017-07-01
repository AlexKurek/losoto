#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Estimate cross-delay

import logging
from losoto.operations_lib import *
logging.debug('Loading CROSSDELAY module.')

def run( step, parset, H ):
    from losoto.h5parm import solFetcher, solWriter
    import numpy as np
    import scipy.optimize

    delaycomplex = lambda d, freq, y: abs(np.cos(d[0]*freq)  - np.cos(y)) + abs(np.sin(d[0]*freq)  - np.sin(y))

    # get involved solsets using local step values or global values or all
    soltabs = getParSoltabs( step, parset, H )

#    refAnt = parset.getString('.'.join(["LoSoTo.Steps", step, "RefAnt"]), '' )
    outTab = parset.getString('.'.join(["LoSoTo.Steps", step, "OutTable"]), 'phasediff' )
    maxres = parset.getFloat('.'.join(["LoSoTo.Steps", step, "MaxResidual"]), 1.)

    for t, soltab in enumerate(openSoltabs( H, soltabs )):
        logging.info("--> Working on soltab: "+soltab._v_name)
        sf = solFetcher(soltab)

        # times and ants needs to be complete or selection is much slower
        times = sf.getAxisValues('time')
        ants = sf.getAxisValues('ant')

        # this will make a selection for the getValues() and getValuesIter()
        userSel = {}
        for axis in sf.getAxesNames():
            userSel[axis] = getParAxis( step, parset, H, axis )
        sf.setSelection(**userSel)

        # some checks
        solType = sf.getType()
        if solType != 'phase':
           logging.warning("Soltab type of "+soltab._v_name+" is of type "+solType+", should be phase. Ignoring.")
           continue

#        if refAnt != '' and not refAnt in ants:
#            logging.error('Reference antenna '+refAnt+' not found.')
#            return 1
#        if refAnt == '': refAnt = ants[0]

        # create new table
        solsetname = soltabs[t].split('/')[0]
        st = H.makeSoltab(solsetname, soltype = sf.getType(), soltab = outTab, axesNames=sf.getAxesNames(), \
                          axesVals=[sf.getAxisValues(axisName) for axisName in sf.getAxesNames()], \
                          vals=sf.getValues(retAxesVals = False), weights=sf.getValues(weight = True, retAxesVals = False), parmdbType=sf.t._v_attrs['parmdb_type'])
        sw = solWriter(st)
        sw.addHistory('Created by CROSSDELAY operation.')
            
#        for vals, weights, coord, selection in sf.getValuesIter(returnAxes=['freq','pol','time'], weight=True, reference = refAnt):
        for vals, weights, coord, selection in sf.getValuesIter(returnAxes=['freq','pol','time'], weight=True):

            fitdelayguess = 1.e-10 # good guess, do not use 0 as it seems the minimizer is unstable with that

            if 'RR' in coord['pol'] and 'LL' in coord['pol']:
                coord1 = np.where(coord['pol'] == 'RR')[0][0]
                coord2 = np.where(coord['pol'] == 'LL')[0][0]
            elif 'XX' in coord['pol'] and 'YY' in coord['pol']:
                coord1 = np.where(coord['pol'] == 'XX')[0][0]
                coord2 = np.where(coord['pol'] == 'YY')[0][0]

#            if not coord['ant'] == refAnt:
            logging.debug('Working on ant: '+coord['ant']+'...')

            if (weights == 0.).all() == True:
                logging.warning('Skipping flagged antenna: '+coord['ant'])
                weights[:] = 0
            else:

                for t, time in enumerate(times):

                    # apply flags
                    idx       = ((weights[coord1,:,t] != 0.) & (weights[coord2,:,t] != 0.))
                    freq      = np.copy(coord['freq'])[idx]
                    phase1    = vals[coord1,:,t][idx]
                    phase2    = vals[coord2,:,t][idx]

                    if len(freq) < 10:
                        vals[:,:,t] = 0.
                        weights[:,:,t] = 0.
                        logging.debug('Not enough unflagged point for the timeslot '+str(t))
                        continue
        
                    if (len(idx) - len(freq))/len(freq) > 1/4.:
                        logging.debug('High number of filtered out data points for the timeslot '+str(t)+': '+str(len(idx) - len(freq)))
        
                    phase_diff  = (phase1 - phase2)
                    phase_diff = np.mod(phase_diff + np.pi, 2.*np.pi) - np.pi
                    #phase_diff[ phase_diff < -np.pi ] += 2*np.pi
                    #phase_diff[ phase_diff > +np.pi ] -= 2*np.pi
    
                    fitresultdelay, success = scipy.optimize.leastsq(delaycomplex, [fitdelayguess], args=(freq, phase_diff))
                    #if t%100==0: print fitresultdelay
                    # fractional residual
                    residual = np.mean(np.abs(np.mod(fitresultdelay*freq-phase_diff + np.pi, 2.*np.pi) - np.pi))

                    #print "t:", t, "result:", fitresultdelay, "residual:", residual

                    if residual < maxres:
                        fitdelayguess = fitresultdelay[0]
                        weight = 1
                    else:       
                        # high residual, flag
                        logging.warning('Bad solution for ant: '+coord['ant']+' (time: '+str(t)+', resdiaul: '+str(residual)+').')
                        weight = 0

                    vals[:,:,t] = 0.
                    vals[coord1,:,t][idx] = fitresultdelay[0]*freq/2.
                    vals[coord2,:,t][idx] = -1.*(fitresultdelay[0]*freq)/2.
                    weights[:,:,t] = 0.
                    weights[coord1,:,t][idx] = weight
                    weights[coord2,:,t][idx] = weight

                    # Debug plot
                    doplot = False
                    if doplot and t%500==0 and coord['ant'] == 'CS004LBA':
                        if not 'matplotlib' in sys.modules:
                            import matplotlib as mpl
                            mpl.rc('font',size =8 )
                            mpl.rc('figure.subplot',left=0.05, bottom=0.05, right=0.95, top=0.95,wspace=0.22, hspace=0.22 )
                            mpl.use("Agg")
                        import matplotlib.pyplot as plt

                        fig = plt.figure()
                        fig.subplots_adjust(wspace=0)
                        ax = fig.add_subplot(111)

                        # plot rm fit
                        plotdelay = lambda delay, freq: np.mod( delay*freq + np.pi, 2.*np.pi) - np.pi
                        ax.plot(freq, plotdelay(fitresultdelay[0], freq), "-", color='purple')

                        ax.plot(freq, np.mod(phase1 + np.pi, 2.*np.pi) - np.pi, 'ob' )
                        ax.plot(freq, np.mod(phase2 + np.pi, 2.*np.pi) - np.pi, 'og' )
                        ax.plot(freq, np.mod(phase_diff + np.pi, 2.*np.pi) - np.pi , '.', color='purple' )                           
     
                        residual = np.mod(plotdelay(fitresultdelay[0], freq)-phase_diff + np.pi,2.*np.pi)-np.pi
                        ax.plot(freq, residual, '.', color='yellow')
        
                        ax.set_xlabel('freq')
                        ax.set_ylabel('phase')
                        ax.set_ylim(ymin=-np.pi, ymax=np.pi)
    
                        logging.warning('Save pic: '+str(t)+'_'+coord['ant']+'.png')
                        plt.savefig(coord['ant']+'_'+str(t)+'.png', bbox_inches='tight')
                        del fig

            sw.setSelection(**coord)
            sw.setValues( vals )
            sw.setValues( weights, weight=True )

        del st
        del sw        
        del sf
    return 0
