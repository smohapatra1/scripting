#   https://www.google.com/search?q=How+will+you+convert+decimal+numbers+between+1+to+3999+to+Roman+numerals%3F+Also%2C+can+you+do+the+reverse%3F+How%3F+python&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifM2rRtB49GXZHkKXqU-Nr9Nt_rrNw%3A1751147938980&udm=50&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIeiAkWG4OlBE2zyCTMjPbGmPzNVD9LjlghyJHnd1ZXeDdPnKMrl0yona68PDS9X-U_cCym5IjWSV9uFOL2q49gMJC8X0CxDgaOYXcFxSkzxpkQh7UYeIBYVy1CTOasP2_6pQRyhDCLHfGlThiPFpvcV39YdEOhUwl-2oCfF1y3ZVVFuMmuA&aep=1&ntc=1&sa=X&ved=2ahUKEwjBlui2jpWOAxUSRDABHZjcCV0Q2J8OegQIFBAC&biw=1729&bih=908&dpr=2&mstk=AUtExfDEeGdq30SXDhAYnDl-Xf7y8604LS0yC1vWV_Bu4JJRitJizBeoLWU3KcPdaAYljMmMTdfgSfdpRRutzesMLWpZ7UGMgUSVSZO8QysssouvFJ__MnZeGbHDzR9oeyPBcx9MAGCpAOsvuCxSpjKuxvKzCwYGcUJETHx1T1V1LrupqyikSkCZBD2nxN_L-46ZfJqJaBMyAOd4wBWzR42aq3wxuxZcFSk9U9ngsuijmifi_X23L0hlZSxLkobd14zwEGSdMQ2p2lrkNlKqb9DT8G5OjdbTVTXQmMxwrX5Asn3577Zx4h5Ba5bCUy0GjWCEOZZzWVbXD7dH3Q&csuir=1

roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roman_to_decimal(roman_numeral):
    result = 0
    for i in range(len(roman_numeral)):
        current_value = roman_dict[roman_numeral[i]]

        if i + 1 < len(roman_numeral) and current_value < roman_dict[roman_numeral[i+1]]:
            result -= current_value
        else:
            result += current_value

    return result


print (roman_to_decimal(3999))



