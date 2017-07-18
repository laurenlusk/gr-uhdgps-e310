#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Uhdgps Rssi Log
# Generated: Thu Jul 13 17:06:38 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import es
import frequency_hopper
import pmt
import sys
import time
import uhdgps
from gnuradio import qtgui


class uhdgps_rssi_log(gr.top_block, Qt.QWidget):

    def __init__(self, div=200, fc=683e6, gain=0, samp_rate=6e6):
        gr.top_block.__init__(self, "Uhdgps Rssi Log")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Uhdgps Rssi Log")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "uhdgps_rssi_log")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.div = div
        self.fc = fc
        self.gain = gain
        self.samp_rate = samp_rate

        ##################################################
        # Blocks
        ##################################################
        self.uhdgps_meta_to_json_file_0 = uhdgps.meta_to_json_file('/tmp/WAMU_RSSI_all_the_test%(time)s.json')
        self.uhdgps_cpdu_average_power_0 = uhdgps.cpdu_average_power(-60)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("addr=192.168.10.7", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_clock_rate(120e6, uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(fc, 0)
        self.uhd_usrp_source_0.set_gain(gain, 0)
        self.frequency_hopper_frequency_sweeper_0 = frequency_hopper.frequency_sweeper(fc, 6e6, 887e6)
        self.es_trigger_sample_timer_0 = es.trigger_sample_timer(gr.sizeof_gr_complex, int(samp_rate)/div, int(3e3), int(samp_rate)/div, 1024 )
        self.es_sink_0 = es.sink(1*[gr.sizeof_gr_complex],8,64,2,2,0)
        self.es_handler_pdu_0 = es.es_make_handler_pdu(es.es_handler_print.TYPE_C32)
        self.blocks_pdu_remove_0 = blocks.pdu_remove(pmt.intern("es::event_buffer"))
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.intern("TEST"), 1e6/div)
        self.blocks_message_debug_0 = blocks.message_debug()

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.frequency_hopper_frequency_sweeper_0, 'clock'))
        self.msg_connect((self.blocks_pdu_remove_0, 'pdus'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.blocks_pdu_remove_0, 'pdus'), (self.uhdgps_meta_to_json_file_0, 'pdus'))
        self.msg_connect((self.es_handler_pdu_0, 'pdus_out'), (self.uhdgps_cpdu_average_power_0, 'cpdus'))
        self.msg_connect((self.es_trigger_sample_timer_0, 'sample_timer_event'), (self.es_handler_pdu_0, 'handle_event'))
        self.msg_connect((self.es_trigger_sample_timer_0, 'which_stream'), (self.es_sink_0, 'schedule_event'))
        self.msg_connect((self.frequency_hopper_frequency_sweeper_0, 'msg_out'), (self.uhd_usrp_source_0, 'command'))
        self.msg_connect((self.uhdgps_cpdu_average_power_0, 'cpdus'), (self.blocks_pdu_remove_0, 'pdus'))
        self.connect((self.es_trigger_sample_timer_0, 0), (self.es_sink_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.es_trigger_sample_timer_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "uhdgps_rssi_log")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_div(self):
        return self.div

    def set_div(self, div):
        self.div = div
        self.blocks_message_strobe_0.set_period(1e6/self.div)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.uhd_usrp_source_0.set_center_freq(self.fc, 0)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.uhd_usrp_source_0.set_gain(self.gain, 0)


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--div", dest="div", type="intx", default=200,
        help="Set div [default=%default]")
    parser.add_option(
        "", "--fc", dest="fc", type="eng_float", default=eng_notation.num_to_str(683e6),
        help="Set fc [default=%default]")
    parser.add_option(
        "", "--gain", dest="gain", type="intx", default=0,
        help="Set gain [default=%default]")
    parser.add_option(
        "", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(6e6),
        help="Set samp_rate [default=%default]")
    return parser


def main(top_block_cls=uhdgps_rssi_log, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(div=options.div, fc=options.fc, gain=options.gain, samp_rate=options.samp_rate)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
