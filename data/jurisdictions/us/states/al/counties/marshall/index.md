---
type: Jurisdiction
title: "Marshall County, AL"
classification: county
fips: "01095"
state: "AL"
demographics:
  population: 99748
  population_under_18: 25941
  population_18_64: 56757
  population_65_plus: 17050
  median_household_income: 62571
  poverty_rate: 16.64
  homeownership_rate: 75.77
  unemployment_rate: 3.91
  median_home_value: 201500
  gini_index: 0.4646
  vacancy_rate: 12.7
  race_white: 78468
  race_black: 2591
  race_asian: 606
  race_native: 1321
  hispanic: 17192
  bachelors_plus: 18815
districts:
  - to: "us/states/al/districts/04"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/al/districts/senate/9"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/al/districts/house/27"
    rel: in-district
    area_weight: 0.7427
  - to: "us/states/al/districts/house/26"
    rel: in-district
    area_weight: 0.257
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Marshall County, AL

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 99748 |
| Under 18 | 25941 |
| 18–64 | 56757 |
| 65+ | 17050 |
| Median household income | 62571 |
| Poverty rate | 16.64 |
| Homeownership rate | 75.77 |
| Unemployment rate | 3.91 |
| Median home value | 201500 |
| Gini index | 0.4646 |
| Vacancy rate | 12.7 |
| White | 78468 |
| Black | 2591 |
| Asian | 606 |
| Native | 1321 |
| Hispanic/Latino | 17192 |
| Bachelor's or higher | 18815 |

## Districts

- [AL-04](/us/states/al/districts/04.md) — 100% (congressional)
- [AL Senate District 9](/us/states/al/districts/senate/9.md) — 100% (state senate)
- [AL House District 27](/us/states/al/districts/house/27.md) — 74% (state house)
- [AL House District 26](/us/states/al/districts/house/26.md) — 26% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
