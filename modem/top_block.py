#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Jul 19 17:40:37 2018
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import time


class top_block(gr.top_block):

    def __init__(self, buffer, baud_rate=38400, samp_rate_tx=4000000, sps=10):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Parameters
        ##################################################
        self.baud_rate = baud_rate
        self.samp_rate_tx = samp_rate_tx
        self.sps = sps

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 384000
        self.freq = freq = 867300000

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate_tx,
                decimation=samp_rate,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_sink_0.set_sample_rate(samp_rate_tx)
        self.osmosdr_sink_0.set_center_freq(freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(30, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)

        self.digital_gfsk_mod_0 = digital.gfsk_mod(
        	samples_per_symbol=sps,
        	sensitivity=1,
        	bt=1,
        	verbose=False,
        	log=False,
        )
        self.blocks_vector_source_x_0 = blocks.vector_source_b(buffer, True, 1, [])
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((800000000, ))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.digital_gfsk_mod_0, 0))
        self.connect((self.digital_gfsk_mod_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))

    def get_baud_rate(self):
        return self.baud_rate

    def set_baud_rate(self, baud_rate):
        self.baud_rate = baud_rate

    def get_samp_rate_tx(self):
        return self.samp_rate_tx

    def set_samp_rate_tx(self, samp_rate_tx):
        self.samp_rate_tx = samp_rate_tx
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate_tx)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.osmosdr_sink_0.set_center_freq(self.freq, 0)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    msg = 'hello jon'
    buffer = bytearray()
    buffer.extend(map(ord, msg))

    # just print out the buffer that has our encoded byte array
    for itm in buffer:
        print itm

    tb = top_block_cls(buffer)
    # at this point it should send the buffer and then exit.
    tb.run()


if __name__ == '__main__':
    main()
