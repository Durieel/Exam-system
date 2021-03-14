# Exam-system
*Krav og tips til løsningen:* <br />
  •	det skal kobles mot databasen via mysql.connector etter følgende «koblingsstreng»: <br />
  
      o mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef ', passwd='oblig2021', db='oblig2021') <br />
      
  •	grensesnittet skal programmeres basert på tkinter-modulen og grid som «geometry manager» <br />
  
  •	Datoer registreres i formatet <år-måned-dag>, dvs 20180510 for 10.05.2018
  
  •	Nye studenter nummereres fortløpende, og applikasjonen skal tildele et nytt studentnr ved å øke største registrerte studentnr med 1. Det skal ikke brukes autoincrement i databasen
  
  •	Vi forutsetter at «en eksamen i et emne» kan gjennomføres på ett rom
  
  Tabellstruktur, databasen oblig2021 :
  
Student(__Studentnr, Fornavn, Etternavn, Epost, Telefon)

Emne(__Emnekode, Emnenavn, Studiepoeng)

Rom(__Romnr, Antallplasser)

Eksamen(__Emnekode*, Dato, Romnr*)

Eksamensresultat(__Studentnr*, Emnekode*, Dato*, Karakter)
	
_	= primærnøkkel/PK
* = fremmednøkkel/FK

Mek den sammensatte fremmednøkkelen fra Eksamensresultat til Eksamen.

Felttyper/lengde Studentnr 
CHAR(6) 
Fornavn CHAR(30) 
Etternavn CHAR(20) 
Epost CHAR(40) 
Telefon CHAR(8)
Emnekode CHAR(8) 
Emnenavn CHAR(40)
Studiepoeng DECIMAL(3,1) 
Romnr CHAR(4)
Antallplasser INTEGER(3)
Dato DATE 
Karakter CHAR(1)

Oppgave: system for håndtering av eksamen ved USN
Det skal programmeres et grafisk basert grensesnitt for applikasjonen og applikasjonen skal kjøre mot en database i MySQL.


Det skal lages en applikasjon for eksamenskontoret ved USN. Applikasjonen skal brukes til planlegging av eksamener og ajourhold av eksamensresultater for studentene.
Det skal være mulig med ajourhold av studenter, eksamen og eksamensresultater.
Det er følgende krav til den nye applikasjonen:

•	kunne ajourholde framtidige eksamener og kontrollere at et rom bare settes opp med en eksamen pr dag
•	utskrift/visning av alle eksamener på en dag, med informasjon om emne og rom
•	utskrift/visning av alle eksamener i en periode, ordnet etter dato med informasjon om emne og rom
•	registrere karakterer for en avholdt eksamen samlet
•	utskrift/visning av alle eksamensresultater i et emne («karakterliste»), dvs alle studenter med oppnådd karakter ordnet etter studentnr
•	utskrift/visning av karakterstatistikk for en gjennomført eksamen i et emne med emneopplysninger og en opptelling av antall kandidater på hver karakter («karakterfordeling»)
•	utskrift av alle eksamensresultater med emnenavn og antall studiepoeng for en student (hvor en kan ha ett eller flere eksamensresultater i samme emne), ordnet etter eksamensdato
•	utskrift av vitnemål for en student. Ved flere avlagte eksamener i samme emne skal kun ett/beste resultat komme på vitnemålet. 
Emnene sorteres på fagnivå og emnekode, dvs alle emnekoder i 1000-serien sorteres og kommer før alle emnekodene i 2000-serien osv. 
Vitnemålet må ha en summering av antall oppnådde studiepoeng for beståtte emner


