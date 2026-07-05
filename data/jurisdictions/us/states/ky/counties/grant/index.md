---
type: Jurisdiction
title: "Grant County, KY"
classification: county
fips: "21081"
state: "KY"
demographics:
  population: 25418
  population_under_18: 6735
  population_18_64: 14993
  population_65_plus: 3690
  median_household_income: 69178
  poverty_rate: 11.73
  homeownership_rate: 75.13
  unemployment_rate: 4.91
  median_home_value: 209500
  gini_index: 0.4034
  vacancy_rate: 9.97
  race_white: 23544
  race_black: 218
  race_asian: 146
  race_native: 17
  hispanic: 824
  bachelors_plus: 3505
districts:
  - to: "us/states/ky/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/17"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ky/districts/house/61"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Grant County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25418 |
| Under 18 | 6735 |
| 18–64 | 14993 |
| 65+ | 3690 |
| Median household income | 69178 |
| Poverty rate | 11.73 |
| Homeownership rate | 75.13 |
| Unemployment rate | 4.91 |
| Median home value | 209500 |
| Gini index | 0.4034 |
| Vacancy rate | 9.97 |
| White | 23544 |
| Black | 218 |
| Asian | 146 |
| Native | 17 |
| Hispanic/Latino | 824 |
| Bachelor's or higher | 3505 |

## Districts

- [KY-04](/us/states/ky/districts/04.md) — 100% (congressional)
- [KY Senate District 17](/us/states/ky/districts/senate/17.md) — 100% (state senate)
- [KY House District 61](/us/states/ky/districts/house/61.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
