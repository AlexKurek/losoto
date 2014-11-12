#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This operation reset all the selected amplitudes to 1
# and all other selected solution types to 0
# WEIGHT: no need to be weight compliant

from operations_lib import *
import logging

logging.debug('Loading RESET module.')

def run( step, parset, H ):

   from h5parm import solWriter

   soltabs = getParSoltabs( step, parset, H )

   setWeight = parset.getBool('.'.join(["LoSoTo.Steps", step, "Weight"]), False )

   for soltab in openSoltabs( H, soltabs ):

        logging.info("Resetting soltab: "+soltab._v_name)

        t = solWriter(soltab)

        # axis selection
        userSel = {}
        for axis in t.getAxesNames():
            userSel[axis] = getParAxis( step, parset, H, axis )
        t.setSelection(**userSel)

        solType = t.getType()

        if setWeight:
            t.setValues(1., weight=setWeight)
        elif solType == 'amplitude':
            t.setValues(1.)
        else:
            t.setValues(0.)

        t.addHistory('RESET')
   return 0
