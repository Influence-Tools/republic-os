---
type: Jurisdiction
title: "Webster County, WV"
classification: county
fips: "54101"
state: "WV"
demographics:
  population: 8144
  population_under_18: 1638
  population_18_64: 4461
  population_65_plus: 2045
  median_household_income: 43839
  poverty_rate: 23.27
  homeownership_rate: 77.3
  unemployment_rate: 9.19
  median_home_value: 76100
  gini_index: 0.4896
  vacancy_rate: 33.93
  race_white: 7604
  race_black: 11
  race_asian: 0
  race_native: 0
  hispanic: 66
  bachelors_plus: 955
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/wv/districts/senate/11"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wv/districts/house/48"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Webster County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8144 |
| Under 18 | 1638 |
| 18–64 | 4461 |
| 65+ | 2045 |
| Median household income | 43839 |
| Poverty rate | 23.27 |
| Homeownership rate | 77.3 |
| Unemployment rate | 9.19 |
| Median home value | 76100 |
| Gini index | 0.4896 |
| Vacancy rate | 33.93 |
| White | 7604 |
| Black | 11 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 66 |
| Bachelor's or higher | 955 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 11](/us/states/wv/districts/senate/11.md) — 100% (state senate)
- [WV House District 48](/us/states/wv/districts/house/48.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
