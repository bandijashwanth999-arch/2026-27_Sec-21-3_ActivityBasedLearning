# Case Study 7: Text Compression Using Character Runs (Run-Length Encoding)
# Goal: replace repeated characters by character + count, e.g. aaab -> a3b1.
# Show whether the encoded text is actually shorter.

samples = ["aaabbbcccd", "abcd", "aaaaaaaaaaaa", "AAaa", "wwwwwbbbw", ""]

for text in samples:
    print("Original :", repr(text), "(length " + str(len(text)) + ")")

    if text == "":
        print("Result   : Empty string - nothing to encode")
        print()
        continue

    encoded = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count = count + 1                       # same character, extend the run
        else:
            encoded = encoded + text[i - 1] + str(count)   # save finished run
            count = 1
    encoded = encoded + text[-1] + str(count)       # save the last run

    print("Encoded  :", encoded, "(length " + str(len(encoded)) + ")")
    if len(encoded) < len(text):
        saved = len(text) - len(encoded)
        print("Result   : Compression is useful, saved", saved, "characters")
    else:
        print("Result   : Encoding NOT beneficial, keep the original text")
    print()
