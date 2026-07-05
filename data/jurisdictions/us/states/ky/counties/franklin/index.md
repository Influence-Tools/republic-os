---
type: Jurisdiction
title: "Franklin County, KY"
classification: county
fips: "21073"
state: "KY"
demographics:
  population: 51842
  population_under_18: 10864
  population_18_64: 31282
  population_65_plus: 9696
  median_household_income: 65298
  poverty_rate: 13.63
  homeownership_rate: 64.47
  unemployment_rate: 5.91
  median_home_value: 216600
  gini_index: 0.452
  vacancy_rate: 5.98
  race_white: 42112
  race_black: 4782
  race_asian: 922
  race_native: 60
  hispanic: 2281
  bachelors_plus: 16374
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.9967
  - to: "us/states/ky/districts/senate/20"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ky/districts/house/57"
    rel: in-district
    area_weight: 0.6077
  - to: "us/states/ky/districts/house/56"
    rel: in-district
    area_weight: 0.3919
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Franklin County, KY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 51842 |
| Under 18 | 10864 |
| 18–64 | 31282 |
| 65+ | 9696 |
| Median household income | 65298 |
| Poverty rate | 13.63 |
| Homeownership rate | 64.47 |
| Unemployment rate | 5.91 |
| Median home value | 216600 |
| Gini index | 0.452 |
| Vacancy rate | 5.98 |
| White | 42112 |
| Black | 4782 |
| Asian | 922 |
| Native | 60 |
| Hispanic/Latino | 2281 |
| Bachelor's or higher | 16374 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 20](/us/states/ky/districts/senate/20.md) — 100% (state senate)
- [KY House District 57](/us/states/ky/districts/house/57.md) — 61% (state house)
- [KY House District 56](/us/states/ky/districts/house/56.md) — 39% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
