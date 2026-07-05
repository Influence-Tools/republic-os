---
type: Jurisdiction
title: "Clay County, AL"
classification: county
fips: "01027"
state: "AL"
demographics:
  population: 14192
  population_under_18: 2974
  population_18_64: 8300
  population_65_plus: 2918
  median_household_income: 55250
  poverty_rate: 17.55
  homeownership_rate: 79.43
  unemployment_rate: 2.4
  median_home_value: 156700
  gini_index: 0.4447
  vacancy_rate: 18.1
  race_white: 11357
  race_black: 1818
  race_asian: 54
  race_native: 24
  hispanic: 465
  bachelors_plus: 1939
districts:
  - to: "us/states/al/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/al/districts/senate/13"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/al/districts/house/35"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Clay County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14192 |
| Under 18 | 2974 |
| 18–64 | 8300 |
| 65+ | 2918 |
| Median household income | 55250 |
| Poverty rate | 17.55 |
| Homeownership rate | 79.43 |
| Unemployment rate | 2.4 |
| Median home value | 156700 |
| Gini index | 0.4447 |
| Vacancy rate | 18.1 |
| White | 11357 |
| Black | 1818 |
| Asian | 54 |
| Native | 24 |
| Hispanic/Latino | 465 |
| Bachelor's or higher | 1939 |

## Districts

- [AL-03](/us/states/al/districts/03.md) — 100% (congressional)
- [AL Senate District 13](/us/states/al/districts/senate/13.md) — 100% (state senate)
- [AL House District 35](/us/states/al/districts/house/35.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
