---
type: Jurisdiction
title: "Lander County, NV"
classification: county
fips: "32015"
state: "NV"
demographics:
  population: 5770
  population_under_18: 1591
  population_18_64: 3330
  population_65_plus: 849
  median_household_income: 89014
  poverty_rate: 10.74
  homeownership_rate: 77.41
  unemployment_rate: 9.4
  median_home_value: 213800
  gini_index: 0.3861
  vacancy_rate: 22.27
  race_white: 4480
  race_black: 71
  race_asian: 36
  race_native: 186
  hispanic: 971
  bachelors_plus: 1126
districts:
  - to: "us/states/nv/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nv/districts/senate/14"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nv/districts/house/32"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nv]
timestamp: "2026-07-03"
---

# Lander County, NV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5770 |
| Under 18 | 1591 |
| 18–64 | 3330 |
| 65+ | 849 |
| Median household income | 89014 |
| Poverty rate | 10.74 |
| Homeownership rate | 77.41 |
| Unemployment rate | 9.4 |
| Median home value | 213800 |
| Gini index | 0.3861 |
| Vacancy rate | 22.27 |
| White | 4480 |
| Black | 71 |
| Asian | 36 |
| Native | 186 |
| Hispanic/Latino | 971 |
| Bachelor's or higher | 1126 |

## Districts

- [NV-02](/us/states/nv/districts/02.md) — 100% (congressional)
- [NV Senate District 14](/us/states/nv/districts/senate/14.md) — 100% (state senate)
- [NV House District 32](/us/states/nv/districts/house/32.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
