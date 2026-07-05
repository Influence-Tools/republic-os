---
type: Jurisdiction
title: "San Joaquin County, CA"
classification: county
fips: "06077"
state: "CA"
demographics:
  population: 797334
  population_under_18: 208824
  population_18_64: 480780
  population_65_plus: 107730
  median_household_income: 92179
  poverty_rate: 12.41
  homeownership_rate: 61.99
  unemployment_rate: 7.57
  median_home_value: 530700
  gini_index: 0.4375
  vacancy_rate: 5.73
  race_white: 254518
  race_black: 54932
  race_asian: 148289
  race_native: 11882
  hispanic: 339161
  bachelors_plus: 154334
districts:
  - to: "us/states/ca/districts/09"
    rel: in-district
    area_weight: 0.8359
  - to: "us/states/ca/districts/13"
    rel: in-district
    area_weight: 0.1604
  - to: "us/states/ca/districts/senate/5"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ca/districts/house/9"
    rel: in-district
    area_weight: 0.6572
  - to: "us/states/ca/districts/house/13"
    rel: in-district
    area_weight: 0.3427
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# San Joaquin County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 797334 |
| Under 18 | 208824 |
| 18–64 | 480780 |
| 65+ | 107730 |
| Median household income | 92179 |
| Poverty rate | 12.41 |
| Homeownership rate | 61.99 |
| Unemployment rate | 7.57 |
| Median home value | 530700 |
| Gini index | 0.4375 |
| Vacancy rate | 5.73 |
| White | 254518 |
| Black | 54932 |
| Asian | 148289 |
| Native | 11882 |
| Hispanic/Latino | 339161 |
| Bachelor's or higher | 154334 |

## Districts

- [CA-09](/us/states/ca/districts/09.md) — 84% (congressional)
- [CA-13](/us/states/ca/districts/13.md) — 16% (congressional)
- [CA Senate District 5](/us/states/ca/districts/senate/5.md) — 100% (state senate)
- [CA House District 9](/us/states/ca/districts/house/9.md) — 66% (state house)
- [CA House District 13](/us/states/ca/districts/house/13.md) — 34% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
