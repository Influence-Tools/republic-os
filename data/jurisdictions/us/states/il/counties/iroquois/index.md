---
type: Jurisdiction
title: "Iroquois County, IL"
classification: county
fips: "17075"
state: "IL"
demographics:
  population: 26449
  population_under_18: 5703
  population_18_64: 14769
  population_65_plus: 5977
  median_household_income: 66255
  poverty_rate: 12.5
  homeownership_rate: 80.0
  unemployment_rate: 4.47
  median_home_value: 137800
  gini_index: 0.4341
  vacancy_rate: 10.52
  race_white: 23481
  race_black: 213
  race_asian: 89
  race_native: 137
  hispanic: 2187
  bachelors_plus: 4431
districts:
  - to: "us/states/il/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/senate/53"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/il/districts/house/106"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Iroquois County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26449 |
| Under 18 | 5703 |
| 18–64 | 14769 |
| 65+ | 5977 |
| Median household income | 66255 |
| Poverty rate | 12.5 |
| Homeownership rate | 80.0 |
| Unemployment rate | 4.47 |
| Median home value | 137800 |
| Gini index | 0.4341 |
| Vacancy rate | 10.52 |
| White | 23481 |
| Black | 213 |
| Asian | 89 |
| Native | 137 |
| Hispanic/Latino | 2187 |
| Bachelor's or higher | 4431 |

## Districts

- [IL-02](/us/states/il/districts/02.md) — 100% (congressional)
- [IL Senate District 53](/us/states/il/districts/senate/53.md) — 100% (state senate)
- [IL House District 106](/us/states/il/districts/house/106.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
