---
type: Jurisdiction
title: "Hidalgo County, NM"
classification: county
fips: "35023"
state: "NM"
demographics:
  population: 4041
  population_under_18: 862
  population_18_64: 2236
  population_65_plus: 943
  median_household_income: 48882
  poverty_rate: 23.08
  homeownership_rate: 80.78
  unemployment_rate: 3.5
  median_home_value: 111000
  gini_index: 0.4362
  vacancy_rate: 33.78
  race_white: 2252
  race_black: 0
  race_asian: 39
  race_native: 16
  hispanic: 2303
  bachelors_plus: 701
districts:
  - to: "us/states/nm/districts/02"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/nm/districts/senate/28"
    rel: in-district
    area_weight: 0.9548
  - to: "us/states/nm/districts/senate/35"
    rel: in-district
    area_weight: 0.0446
  - to: "us/states/nm/districts/house/32"
    rel: in-district
    area_weight: 0.9547
  - to: "us/states/nm/districts/house/39"
    rel: in-district
    area_weight: 0.0447
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Hidalgo County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4041 |
| Under 18 | 862 |
| 18–64 | 2236 |
| 65+ | 943 |
| Median household income | 48882 |
| Poverty rate | 23.08 |
| Homeownership rate | 80.78 |
| Unemployment rate | 3.5 |
| Median home value | 111000 |
| Gini index | 0.4362 |
| Vacancy rate | 33.78 |
| White | 2252 |
| Black | 0 |
| Asian | 39 |
| Native | 16 |
| Hispanic/Latino | 2303 |
| Bachelor's or higher | 701 |

## Districts

- [NM-02](/us/states/nm/districts/02.md) — 100% (congressional)
- [NM Senate District 28](/us/states/nm/districts/senate/28.md) — 95% (state senate)
- [NM Senate District 35](/us/states/nm/districts/senate/35.md) — 4% (state senate)
- [NM House District 32](/us/states/nm/districts/house/32.md) — 95% (state house)
- [NM House District 39](/us/states/nm/districts/house/39.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
