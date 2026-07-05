---
type: Jurisdiction
title: "Crawford County, WI"
classification: county
fips: "55023"
state: "WI"
demographics:
  population: 16042
  population_under_18: 3077
  population_18_64: 8933
  population_65_plus: 4032
  median_household_income: 64094
  poverty_rate: 13.78
  homeownership_rate: 77.15
  unemployment_rate: 3.15
  median_home_value: 183400
  gini_index: 0.4258
  vacancy_rate: 23.49
  race_white: 14901
  race_black: 255
  race_asian: 83
  race_native: 46
  hispanic: 314
  bachelors_plus: 2874
districts:
  - to: "us/states/wi/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/senate/17"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/house/49"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Crawford County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16042 |
| Under 18 | 3077 |
| 18–64 | 8933 |
| 65+ | 4032 |
| Median household income | 64094 |
| Poverty rate | 13.78 |
| Homeownership rate | 77.15 |
| Unemployment rate | 3.15 |
| Median home value | 183400 |
| Gini index | 0.4258 |
| Vacancy rate | 23.49 |
| White | 14901 |
| Black | 255 |
| Asian | 83 |
| Native | 46 |
| Hispanic/Latino | 314 |
| Bachelor's or higher | 2874 |

## Districts

- [WI-03](/us/states/wi/districts/03.md) — 100% (congressional)
- [WI Senate District 17](/us/states/wi/districts/senate/17.md) — 100% (state senate)
- [WI House District 49](/us/states/wi/districts/house/49.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
