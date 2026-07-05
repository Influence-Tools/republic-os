---
type: Jurisdiction
title: "Vigo County, IN"
classification: county
fips: "18167"
state: "IN"
demographics:
  population: 106109
  population_under_18: 21761
  population_18_64: 65922
  population_65_plus: 18426
  median_household_income: 52976
  poverty_rate: 19.15
  homeownership_rate: 61.7
  unemployment_rate: 5.72
  median_home_value: 148500
  gini_index: 0.4779
  vacancy_rate: 9.58
  race_white: 89923
  race_black: 6106
  race_asian: 2202
  race_native: 254
  hispanic: 3411
  bachelors_plus: 25266
districts:
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/in/districts/senate/38"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/in/districts/house/42"
    rel: in-district
    area_weight: 0.2729
  - to: "us/states/in/districts/house/46"
    rel: in-district
    area_weight: 0.2576
  - to: "us/states/in/districts/house/43"
    rel: in-district
    area_weight: 0.2458
  - to: "us/states/in/districts/house/45"
    rel: in-district
    area_weight: 0.2236
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Vigo County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 106109 |
| Under 18 | 21761 |
| 18–64 | 65922 |
| 65+ | 18426 |
| Median household income | 52976 |
| Poverty rate | 19.15 |
| Homeownership rate | 61.7 |
| Unemployment rate | 5.72 |
| Median home value | 148500 |
| Gini index | 0.4779 |
| Vacancy rate | 9.58 |
| White | 89923 |
| Black | 6106 |
| Asian | 2202 |
| Native | 254 |
| Hispanic/Latino | 3411 |
| Bachelor's or higher | 25266 |

## Districts

- [IN-08](/us/states/in/districts/08.md) — 100% (congressional)
- [IN Senate District 38](/us/states/in/districts/senate/38.md) — 100% (state senate)
- [IN House District 42](/us/states/in/districts/house/42.md) — 27% (state house)
- [IN House District 46](/us/states/in/districts/house/46.md) — 26% (state house)
- [IN House District 43](/us/states/in/districts/house/43.md) — 25% (state house)
- [IN House District 45](/us/states/in/districts/house/45.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
