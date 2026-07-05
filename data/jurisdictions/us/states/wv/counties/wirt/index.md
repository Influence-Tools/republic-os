---
type: Jurisdiction
title: "Wirt County, WV"
classification: county
fips: "54105"
state: "WV"
demographics:
  population: 5053
  population_under_18: 1070
  population_18_64: 2816
  population_65_plus: 1167
  median_household_income: 49867
  poverty_rate: 16.83
  homeownership_rate: 87.75
  unemployment_rate: 4.95
  median_home_value: 115800
  gini_index: 0.4068
  vacancy_rate: 25.1
  race_white: 4873
  race_black: 0
  race_asian: 11
  race_native: 0
  hispanic: 0
  bachelors_plus: 708
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 0.995
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.005
  - to: "us/states/wv/districts/senate/3"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/wv/districts/house/15"
    rel: in-district
    area_weight: 0.7765
  - to: "us/states/wv/districts/house/14"
    rel: in-district
    area_weight: 0.2227
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Wirt County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5053 |
| Under 18 | 1070 |
| 18–64 | 2816 |
| 65+ | 1167 |
| Median household income | 49867 |
| Poverty rate | 16.83 |
| Homeownership rate | 87.75 |
| Unemployment rate | 4.95 |
| Median home value | 115800 |
| Gini index | 0.4068 |
| Vacancy rate | 25.1 |
| White | 4873 |
| Black | 0 |
| Asian | 11 |
| Native | 0 |
| Hispanic/Latino | 0 |
| Bachelor's or higher | 708 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV-02](/us/states/wv/districts/02.md) — 0% (congressional)
- [WV Senate District 3](/us/states/wv/districts/senate/3.md) — 100% (state senate)
- [WV House District 15](/us/states/wv/districts/house/15.md) — 78% (state house)
- [WV House District 14](/us/states/wv/districts/house/14.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
