---
type: Jurisdiction
title: "El Dorado County, CA"
classification: county
fips: "06017"
state: "CA"
demographics:
  population: 192662
  population_under_18: 37633
  population_18_64: 109775
  population_65_plus: 45254
  median_household_income: 108845
  poverty_rate: 7.99
  homeownership_rate: 77.24
  unemployment_rate: 4.49
  median_home_value: 679900
  gini_index: 0.4699
  vacancy_rate: 19.51
  race_white: 150027
  race_black: 1574
  race_asian: 10497
  race_native: 1069
  hispanic: 27892
  bachelors_plus: 76786
districts:
  - to: "us/states/ca/districts/03"
    rel: in-district
    area_weight: 0.7623
  - to: "us/states/ca/districts/05"
    rel: in-district
    area_weight: 0.2377
  - to: "us/states/ca/districts/senate/4"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ca/districts/house/1"
    rel: in-district
    area_weight: 0.7411
  - to: "us/states/ca/districts/house/5"
    rel: in-district
    area_weight: 0.2589
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# El Dorado County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 192662 |
| Under 18 | 37633 |
| 18–64 | 109775 |
| 65+ | 45254 |
| Median household income | 108845 |
| Poverty rate | 7.99 |
| Homeownership rate | 77.24 |
| Unemployment rate | 4.49 |
| Median home value | 679900 |
| Gini index | 0.4699 |
| Vacancy rate | 19.51 |
| White | 150027 |
| Black | 1574 |
| Asian | 10497 |
| Native | 1069 |
| Hispanic/Latino | 27892 |
| Bachelor's or higher | 76786 |

## Districts

- [CA-03](/us/states/ca/districts/03.md) — 76% (congressional)
- [CA-05](/us/states/ca/districts/05.md) — 24% (congressional)
- [CA Senate District 4](/us/states/ca/districts/senate/4.md) — 100% (state senate)
- [CA House District 1](/us/states/ca/districts/house/1.md) — 74% (state house)
- [CA House District 5](/us/states/ca/districts/house/5.md) — 26% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
