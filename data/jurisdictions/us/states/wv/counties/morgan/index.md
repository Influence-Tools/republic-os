---
type: Jurisdiction
title: "Morgan County, WV"
classification: county
fips: "54065"
state: "WV"
demographics:
  population: 17426
  population_under_18: 2964
  population_18_64: 10076
  population_65_plus: 4386
  median_household_income: 72179
  poverty_rate: 11.17
  homeownership_rate: 84.13
  unemployment_rate: 3.9
  median_home_value: 240600
  gini_index: 0.3767
  vacancy_rate: 20.63
  race_white: 16320
  race_black: 8
  race_asian: 115
  race_native: 0
  hispanic: 310
  bachelors_plus: 3651
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.9963
  - to: "us/states/wv/districts/senate/15"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/wv/districts/house/90"
    rel: in-district
    area_weight: 0.6004
  - to: "us/states/wv/districts/house/89"
    rel: in-district
    area_weight: 0.3984
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Morgan County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17426 |
| Under 18 | 2964 |
| 18–64 | 10076 |
| 65+ | 4386 |
| Median household income | 72179 |
| Poverty rate | 11.17 |
| Homeownership rate | 84.13 |
| Unemployment rate | 3.9 |
| Median home value | 240600 |
| Gini index | 0.3767 |
| Vacancy rate | 20.63 |
| White | 16320 |
| Black | 8 |
| Asian | 115 |
| Native | 0 |
| Hispanic/Latino | 310 |
| Bachelor's or higher | 3651 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 15](/us/states/wv/districts/senate/15.md) — 100% (state senate)
- [WV House District 90](/us/states/wv/districts/house/90.md) — 60% (state house)
- [WV House District 89](/us/states/wv/districts/house/89.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
