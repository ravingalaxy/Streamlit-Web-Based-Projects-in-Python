import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('dna.jpg')
st.image(image, width=600)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query for FASTA format (Nucleotide(ATGC) sequence) !
***
""")

st.header('Enter DNA sequence in FASTA format')
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area("sequence Input", sequence_input, height=300)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***
""")

st.header("Input Nucleotide Sequence")
sequence

st.header("OUTPUT Nucleotide Count")

st.subheader("1. Print Dictionary")

def Nucleotide_count(seq):
    d = {
    'A': seq.count('A'),
    'T': seq.count('T'),
    'G': seq.count('G'),
    'C': seq.count('C'),
    }
    return d

X = Nucleotide_count(sequence)
X

st.subheader("2. Print Human Readable form")
st.write("There are ",X['A']," adenine(A)")
st.write("There are ",X['T']," thymine(T)")
st.write("There are ",X['G']," guanine(G)")
st.write("There are ",X['C']," cytosine(C)")

st.subheader("3. Nucleotide DataFrame")
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0:'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {"index":'nucleotide'})
st.write(df)

st.subheader("4. Bar Chart")
p = alt.Chart(df).mark_bar().encode(x='nucleotide', y='count')
p = p.properties(width=alt.Step(80))
st.write(p)
