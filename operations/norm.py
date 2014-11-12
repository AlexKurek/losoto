#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is an interpolation script for LoSoTo
# WEIGHT: Weights compliant

import logging
from operations_lib import *

logging.debug('Loading NORM module.')

def run( step, parset, H ):
    """
    Normalize the solutions to a given value
    """
    import numpy as np
    from h5parm import solFetcher, solWriter
    
    soltabs = getParSoltabs( step, parset, H )
    solTypes = getParSolTypes( step, parset, H )

    normVal = parset.getFloat('.'.join(["LoSoTo.Steps", step, "NormVal"]), 1. )
    normAxis = parset.getString('.'.join(["LoSoTo.Steps", step, "NormAxis"]), 'time' )
    useWeights = parset.getBool('.'.join(["LoSoTo.Steps", step, "UseWeights"]), True )

    for soltab in openSoltabs( H, soltabs ):
        logging.info("--> Working on soltab: "+soltab._v_name)

        tr = solFetcher(soltab)
        tw = solWriter(soltab)

        axesNames = tr.getAxesNames()
        if normAxis not in axesNames:
            logging.error('Normalization axis '+normAxis+' not found.')
            return 1

        # axis selection
        userSel = {}
        for axis in tr.getAxesNames():
            userSel[axis] = getParAxis( step, parset, H, axis )
        tr.setSelection(**userSel)

        for vals, weights, coord in tr.getValuesIter(returnAxes=normAxis, weight = True):

            # construct grid
            coordSel = removeKeys(coord, normAxis)
            logging.debug("Working on coords:"+str(coordSel))

            if not useWeights:
                weights = None
            
            # rescale solutions
            valsMean = np.average(vals, weights=weights)
            valsNew = normVal*vals/valsMean
            logging.debug("Rescaling by: "+str(normVal/valsMean))

            # writing back the solutions
            tw.setSelection(**coordSel)
            tw.setValues(valsNew)

    tw.addHistory('NORM (on axis %s)' % (normAxis))
    return 0
