---
type: Jurisdiction
title: "Wharton County, TX"
classification: county
fips: "48481"
state: "TX"
demographics:
  population: 41794
  population_under_18: 10622
  population_18_64: 23583
  population_65_plus: 7589
  median_household_income: 66924
  poverty_rate: 13.61
  homeownership_rate: 72.26
  unemployment_rate: 4.86
  median_home_value: 189900
  gini_index: 0.464
  vacancy_rate: 10.28
  race_white: 24009
  race_black: 4779
  race_asian: 209
  race_native: 122
  hispanic: 17560
  bachelors_plus: 7054
districts:
  - to: "us/states/tx/districts/22"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/tx/districts/senate/17"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/85"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Wharton County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 41794 |
| Under 18 | 10622 |
| 18–64 | 23583 |
| 65+ | 7589 |
| Median household income | 66924 |
| Poverty rate | 13.61 |
| Homeownership rate | 72.26 |
| Unemployment rate | 4.86 |
| Median home value | 189900 |
| Gini index | 0.464 |
| Vacancy rate | 10.28 |
| White | 24009 |
| Black | 4779 |
| Asian | 209 |
| Native | 122 |
| Hispanic/Latino | 17560 |
| Bachelor's or higher | 7054 |

## Districts

- [TX-22](/us/states/tx/districts/22.md) — 100% (congressional)
- [TX Senate District 17](/us/states/tx/districts/senate/17.md) — 100% (state senate)
- [TX House District 85](/us/states/tx/districts/house/85.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
