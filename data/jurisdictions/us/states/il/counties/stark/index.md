---
type: Jurisdiction
title: "Stark County, IL"
classification: county
fips: "17175"
state: "IL"
demographics:
  population: 5308
  population_under_18: 1147
  population_18_64: 2946
  population_65_plus: 1215
  median_household_income: 62878
  poverty_rate: 11.05
  homeownership_rate: 80.13
  unemployment_rate: 2.33
  median_home_value: 104500
  gini_index: 0.4482
  vacancy_rate: 11.19
  race_white: 4869
  race_black: 66
  race_asian: 45
  race_native: 5
  hispanic: 152
  bachelors_plus: 1018
districts:
  - to: "us/states/il/districts/16"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/senate/47"
    rel: in-district
    area_weight: 0.6253
  - to: "us/states/il/districts/senate/37"
    rel: in-district
    area_weight: 0.3747
  - to: "us/states/il/districts/house/93"
    rel: in-district
    area_weight: 0.6253
  - to: "us/states/il/districts/house/73"
    rel: in-district
    area_weight: 0.3747
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Stark County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5308 |
| Under 18 | 1147 |
| 18–64 | 2946 |
| 65+ | 1215 |
| Median household income | 62878 |
| Poverty rate | 11.05 |
| Homeownership rate | 80.13 |
| Unemployment rate | 2.33 |
| Median home value | 104500 |
| Gini index | 0.4482 |
| Vacancy rate | 11.19 |
| White | 4869 |
| Black | 66 |
| Asian | 45 |
| Native | 5 |
| Hispanic/Latino | 152 |
| Bachelor's or higher | 1018 |

## Districts

- [IL-16](/us/states/il/districts/16.md) — 100% (congressional)
- [IL Senate District 47](/us/states/il/districts/senate/47.md) — 63% (state senate)
- [IL Senate District 37](/us/states/il/districts/senate/37.md) — 37% (state senate)
- [IL House District 93](/us/states/il/districts/house/93.md) — 63% (state house)
- [IL House District 73](/us/states/il/districts/house/73.md) — 37% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
