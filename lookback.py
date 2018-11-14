import time, math, sys, argparse
import pyaudio, alsaaudio, audioop
from multiprocessing import Process, Queue
from gcoud.credentials import get_credentials
from google.cloud.speech.v1beta1 import cloud_speech_pb2
from grpc.beta import implementations

class stdout:
    BOLD = "\033[1m"
    END = "\033[0m"
    CLEAR = "\033[2k"

