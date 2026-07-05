---
type: Jurisdiction
title: "Harper County, OK"
classification: county
fips: "40059"
state: "OK"
demographics:
  population: 3203
  population_under_18: 763
  population_18_64: 1799
  population_65_plus: 641
  median_household_income: 64053
  poverty_rate: 13.12
  homeownership_rate: 83.57
  unemployment_rate: 2.61
  median_home_value: 99200
  gini_index: 0.4066
  vacancy_rate: 22.23
  race_white: 2345
  race_black: 2
  race_asian: 2
  race_native: 45
  hispanic: 784
  bachelors_plus: 780
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/senate/27"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/61"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Harper County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3203 |
| Under 18 | 763 |
| 18–64 | 1799 |
| 65+ | 641 |
| Median household income | 64053 |
| Poverty rate | 13.12 |
| Homeownership rate | 83.57 |
| Unemployment rate | 2.61 |
| Median home value | 99200 |
| Gini index | 0.4066 |
| Vacancy rate | 22.23 |
| White | 2345 |
| Black | 2 |
| Asian | 2 |
| Native | 45 |
| Hispanic/Latino | 784 |
| Bachelor's or higher | 780 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 27](/us/states/ok/districts/senate/27.md) — 100% (state senate)
- [OK House District 61](/us/states/ok/districts/house/61.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
