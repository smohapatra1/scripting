#   https://www.google.com/search?q=%27The+sky+is+dark+blue.%27+Can+you+reverse+the+order+of+this+string+in+python&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifOrIqHFtncYwtw9ShKIXYAfR9aBIg%3A1750786899982&udm=50&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZud1z6kQpMfoEdCJxnpm_3WBcADgXS0kQ7L92bqYkFCG8OseL5EwP8OoDpZDtG5HGiruM7n7VOPSE3Dg6dWbXapVkuhOOCEubw4P_EDYwCkm-BbqgtiqVkdKPeJmy0oCga0uv96kS3WVTcMC2hNa72GHyh7c63ZI0uhNQXocLocy3V99zf15jApuEBFilFS8Hn1l_Yw&aep=1&ntc=1&sa=X&ved=2ahUKEwilzIC6zYqOAxU1le4BHUXDKfAQ2J8OegQIEhAC&biw=1729&bih=876&dpr=2&mstk=AUtExfB2xgU1yQD6FrQCCQFDzAaTrKwifA5QxKKeFVYG245A97WC96uW36gX5oetE7fXMK6jamnDl1-IVJjIyG3Ngsi0hpHsduoYxA_exwckUuv_vnq4-wqcMoBrLBgM81b9Ux3VtlKn9WpnL0T4DgAwOmbargq0yMy4tlwRj5tWeMWRo7AcY9c5pKK6eZwFGkOuiCBEGut1Cgsop1NBjeonMeGJuYG7cIao3csIWkmNOGJX12JtaQ05WIwaiDn4WoY78ZhD8G4zxNMXH-6DyUvTW2rlJ-RBrWth_4jvtKBHwEXqAm-FARu7ulCs0Lp2qFkTxHhXGuiQ7fkpzQ&csuir=1

string = "the sky is dark blue"
string2 = string[::-1]
string3 = "".join(reversed(string))
print (string2)
print (string3)