---
type: Jurisdiction
title: "Roger Mills County, OK"
classification: county
fips: "40129"
state: "OK"
demographics:
  population: 3359
  population_under_18: 815
  population_18_64: 1793
  population_65_plus: 751
  median_household_income: 66094
  poverty_rate: 14.67
  homeownership_rate: 83.12
  unemployment_rate: 3.19
  median_home_value: 157800
  gini_index: 0.4559
  vacancy_rate: 23.34
  race_white: 2792
  race_black: 9
  race_asian: 10
  race_native: 229
  hispanic: 287
  bachelors_plus: 752
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/27"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/57"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Roger Mills County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3359 |
| Under 18 | 815 |
| 18–64 | 1793 |
| 65+ | 751 |
| Median household income | 66094 |
| Poverty rate | 14.67 |
| Homeownership rate | 83.12 |
| Unemployment rate | 3.19 |
| Median home value | 157800 |
| Gini index | 0.4559 |
| Vacancy rate | 23.34 |
| White | 2792 |
| Black | 9 |
| Asian | 10 |
| Native | 229 |
| Hispanic/Latino | 287 |
| Bachelor's or higher | 752 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 27](/us/states/ok/districts/senate/27.md) — 100% (state senate)
- [OK House District 57](/us/states/ok/districts/house/57.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
