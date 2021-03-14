# Exam-system
*Krav og tips til løsningen:* <br />
  •	det skal kobles mot databasen via mysql.connector etter følgende «koblingsstreng»: <br />
  
      o mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef ', passwd='oblig2021', db='oblig2021') <br />
      
  •	grensesnittet skal programmeres basert på tkinter-modulen og grid som «geometry manager» <br />
  
  •	Datoer registreres i formatet <år-måned-dag>, dvs 20180510 for 10.05.2018 <br />
  
  •	Nye studenter nummereres fortløpende, og applikasjonen skal tildele et nytt studentnr ved å øke største registrerte studentnr med 1. Det skal ikke brukes autoincrement i databasen <br />
  
  •	Vi forutsetter at «en eksamen i et emne» kan gjennomføres på ett rom <br />
  
  Tabellstruktur, databasen oblig2021 : <br />
  
Student(__Studentnr, Fornavn, Etternavn, Epost, Telefon) <br />

Emne(__Emnekode, Emnenavn, Studiepoeng) <br />

Rom(__Romnr, Antallplasser) <br />

Eksamen(__Emnekode*, Dato, Romnr*) <br />

Eksamensresultat(__Studentnr*, Emnekode*, Dato*, Karakter) <br />
	
_	= primærnøkkel/PK 
* = fremmednøkkel/FK

Mek den sammensatte fremmednøkkelen fra Eksamensresultat til Eksamen.<br />

Felttyper/lengde Studentnr  <br />
CHAR(6) <br />
Fornavn CHAR(30) <br />
Etternavn CHAR(20) <br />
Epost CHAR(40) <br />
Telefon CHAR(8)<br />
Emnekode CHAR(8) <br />
Emnenavn CHAR(40)<br />
Studiepoeng DECIMAL(3,1) <br />
Romnr CHAR(4)<br />
Antallplasser INTEGER(3)<br />
Dato DATE <br />
Karakter CHAR(1)<br />

Oppgave: system for håndtering av eksamen ved USN<br />
Det skal programmeres et grafisk basert grensesnitt for applikasjonen og applikasjonen skal kjøre mot en database i MySQL.<br />


Det skal lages en applikasjon for eksamenskontoret ved USN. Applikasjonen skal brukes til planlegging av eksamener og ajourhold av eksamensresultater for studentene.<br />
Det skal være mulig med ajourhold av studenter, eksamen og eksamensresultater.<br />
Det er følgende krav til den nye applikasjonen:<br />

•	kunne ajourholde framtidige eksamener og kontrollere at et rom bare settes opp med en eksamen pr dag<br />
•	utskrift/visning av alle eksamener på en dag, med informasjon om emne og rom<br />
•	utskrift/visning av alle eksamener i en periode, ordnet etter dato med informasjon om emne og rom<br />
•	registrere karakterer for en avholdt eksamen samlet<br />
•	utskrift/visning av alle eksamensresultater i et emne («karakterliste»), dvs alle studenter med oppnådd karakter ordnet etter studentnr<br />
•	utskrift/visning av karakterstatistikk for en gjennomført eksamen i et emne med emneopplysninger og en opptelling av antall kandidater på hver karakter («karakterfordeling»)<br />
•	utskrift av alle eksamensresultater med emnenavn og antall studiepoeng for en student (hvor en kan ha ett eller flere eksamensresultater i samme emne), ordnet etter eksamensdato<br />
•	utskrift av vitnemål for en student. Ved flere avlagte eksamener i samme emne skal kun ett/beste resultat komme på vitnemålet. <br />
Emnene sorteres på fagnivå og emnekode, dvs alle emnekoder i 1000-serien sorteres og kommer før alle emnekodene i 2000-serien osv. <br />
Vitnemålet må ha en summering av antall oppnådde studiepoeng for beståtte emner<br />


