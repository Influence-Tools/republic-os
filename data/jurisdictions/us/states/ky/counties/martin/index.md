---
type: Jurisdiction
title: "Martin County, KY"
classification: county
fips: "21159"
state: "KY"
demographics:
  population: 11027
  population_under_18: 2179
  population_18_64: 6876
  population_65_plus: 1972
  median_household_income: 37042
  poverty_rate: 33.17
  homeownership_rate: 84.9
  unemployment_rate: 5.46
  median_home_value: 86900
  gini_index: 0.5715
  vacancy_rate: 20.73
  race_white: 9489
  race_black: 874
  race_asian: 0
  race_native: 40
  hispanic: 189
  bachelors_plus: 1221
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 0.99
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 0.01
  - to: "us/states/ky/districts/senate/31"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ky/districts/house/97"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Martin County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11027 |
| Under 18 | 2179 |
| 18–64 | 6876 |
| 65+ | 1972 |
| Median household income | 37042 |
| Poverty rate | 33.17 |
| Homeownership rate | 84.9 |
| Unemployment rate | 5.46 |
| Median home value | 86900 |
| Gini index | 0.5715 |
| Vacancy rate | 20.73 |
| White | 9489 |
| Black | 874 |
| Asian | 0 |
| Native | 40 |
| Hispanic/Latino | 189 |
| Bachelor's or higher | 1221 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 99% (congressional)
- [WV-01](/us/states/wv/districts/01.md) — 1% (congressional)
- [KY Senate District 31](/us/states/ky/districts/senate/31.md) — 100% (state senate)
- [KY House District 97](/us/states/ky/districts/house/97.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
