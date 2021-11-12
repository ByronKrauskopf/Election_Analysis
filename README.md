# Election_Analysis

## Project Overview 
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Get a complete list of counties where votes were cast.
4. Calculate the total number of votes each candidate received.
5. Calculate the total number of votes cast in each county.
6. Calculate the percentage of votes each candidate won.
7. Calculate the percentage of votes cast in each county.
8. Determine the winner of the election based on popluar vote.
9. Determine the county with the highest number of votes cast.

Furthermore, a request has been made to provide an analysis of script used to conduct this election audit to determine if it can be used to conduct audits of other elections. 

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.8, Visual Studio Code 1.62.0

## Summary of Election Audit Results
The analysis of the election show that:
 - There were 369,711 votes cast in the election.
 - The counties where votes were cast were:
    - Jefferson
    - Denver
    - Arapahoe
 - The county results were:
    - Jefferson received 10.5% of the vote and 38,855 number of votes.
    - Denver recevied 82.8% of the vote and 306,055 number of votes.
    - Arapahoe received 6.7% of the vote and 24,801 number of votes.
 - The county with the number of votes cast was:
    - Denver. which received 82.8% of the vote and 306,055 number of votes.
 - The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
 - The candidate results were:
    - Charles Casper Stockman received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the votes and 272,892 number of votes.
    - Raymon Anthony Doane recived 3.1% of the votes and 11,606 number of votes.
 - The winner of the election was:
    - Diana DeGette, who received 73.8% of the votes and 272,892 number of votes.

## Summary of Election Audit Analysis
The script used for this election audit can easily be used for other elections whether they are other Colorado congressional elections or not . The primary reason for this is that none of the variables, such as candidate name, are hardcoded into the script. Rather they are populated directly from the source document. An example of this is below.


