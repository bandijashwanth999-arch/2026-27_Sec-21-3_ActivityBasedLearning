# University Scholarship Allocation (Case Study 1)

## 1. Problem Statement
A university offers a limited number of scholarships. Each applicant has aggregate marks, a lowest subject mark, attendance and family income. The system must check every applicant against the eligibility rules, rank the eligible students, and resolve ties using fixed rules.

## 2. Objectives
- Validate each applicant against four criteria (aggregate, subject minimum, attendance, income).
- Report the exact reason(s) for rejection.
- Rank eligible students using a main rule and tie-break rules.
- Award scholarships to the top students within the quota; others go to the waiting list.

## 3. Assumptions
- Aggregate, subject minimum and attendance are percentages (0-100); income is yearly, in rupees.
- Policy: aggregate >= 75, every subject >= 50, attendance >= 75, income <= 3,00,000, quota = 3.
- Ranking: higher aggregate first; tie -> higher attendance; still tied -> lower income.
- Input data is stored in the program (list of tuples) and is assumed to be correct numbers.

## 4. Algorithm
1. Start and store policy values and the applicant list.
2. For each applicant, unpack the tuple and test the four rules; collect reasons for failure.
3. If there are no reasons, add the applicant to the eligible list; otherwise print the reasons.
4. Sort the eligible list with bubble sort using the three ranking rules.
5. Print the rank list; rank <= quota is AWARDED, the rest are WAITING LIST.
6. Stop.
## 5. Conclusion
The program evaluates applicants with conditional statements, shows the reason for every rejection, and ranks the eligible students using a bubble sort with three tie-breaking rules. It uses lists, tuples and tuple unpacking from the syllabus. The policy values are stored in variables, so a different policy can be tested by changing one line.
