---
type: Jurisdiction
title: "Wyoming County, WV"
classification: county
fips: "54109"
state: "WV"
demographics:
  population: 20629
  population_under_18: 4132
  population_18_64: 11660
  population_65_plus: 4837
  median_household_income: 48440
  poverty_rate: 22.58
  homeownership_rate: 82.47
  unemployment_rate: 5.65
  median_home_value: 82900
  gini_index: 0.4209
  vacancy_rate: 18.94
  race_white: 19982
  race_black: 55
  race_asian: 17
  race_native: 0
  hispanic: 167
  bachelors_plus: 2825
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wv/districts/senate/9"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/wv/districts/house/35"
    rel: in-district
    area_weight: 0.8924
  - to: "us/states/wv/districts/house/43"
    rel: in-district
    area_weight: 0.1069
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Wyoming County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20629 |
| Under 18 | 4132 |
| 18–64 | 11660 |
| 65+ | 4837 |
| Median household income | 48440 |
| Poverty rate | 22.58 |
| Homeownership rate | 82.47 |
| Unemployment rate | 5.65 |
| Median home value | 82900 |
| Gini index | 0.4209 |
| Vacancy rate | 18.94 |
| White | 19982 |
| Black | 55 |
| Asian | 17 |
| Native | 0 |
| Hispanic/Latino | 167 |
| Bachelor's or higher | 2825 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 9](/us/states/wv/districts/senate/9.md) — 100% (state senate)
- [WV House District 35](/us/states/wv/districts/house/35.md) — 89% (state house)
- [WV House District 43](/us/states/wv/districts/house/43.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
