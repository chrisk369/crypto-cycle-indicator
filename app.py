import streamlit as st
import requests
import pandas as pd
import numpy as np
from datetime import datetime
from pytrends.request import TrendReq
import time

st.set_page_config(page_title="🧠 Crypto Cycle Top Indicator", layout="wide")
st.title("🧠 Crypto Cycle Top Indicator")
st.caption("Combining sentiment, price, and on-chain signals to spot potential cycle tops")
