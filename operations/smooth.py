#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This operation for LoSoTo implement a smoothing function
# WEIGHH: not ready

import logging
from operations_lib import *

logging.debug('Loading SMOOTH module.')

def run( step, parset, H ):

    import scipy.ndimage.filters
    from h5parm import solFetcher, solWriter

    soltabs = getParSoltabs( step, parset, H )

    axesToSmooth = parset.getStringVector('.'.join(["LoSoTo.Steps", step, "Axes"]), [] )
    FWHM = parset.getIntVector('.'.join(["LoSoTo.Steps", step, "FWHM"]), [] )

    if len(axesToSmooth) != len(FWHM):
        logging.error("Axes and FWHM lenghts must be equal.")
        return 1

    for soltab in openSoltabs( H, soltabs ):

        logging.info("Smoothing soltab: "+soltab._v_name)

        sf = solFetcher(soltab)
        sw = solWriter(soltab, useCache = True) # remember to flush!

        # axis selection
        userSel = {}
        for axis in sf.getAxesNames():
            userSel[axis] = getParAxis( step, parset, H, axis )
        sf.setSelection(**userSel)

        for i, axis in enumerate(axesToSmooth[:]):
            if axis not in sf.getAxesNames():
                del axesToSmooth[i]
                del FWHM[i]
                logging.warning('Axis \"'+axis+'\" not found. Ignoring.')

        for vals, coord in sf.getValuesIter(returnAxes=axesToSmooth):

            valsnew = scipy.ndimage.filters.median_filter(vals, FWHM)
            coord = removeKeys(coord, axesToSmooth)
            sw.setSelection(**coord)
            sw.setValues(valsnew)

        sw.flush()
        sw.addHistory('SMOOTH (over %s with box size = %s)' % (axesToSmooth, FWHM))
    return 0


