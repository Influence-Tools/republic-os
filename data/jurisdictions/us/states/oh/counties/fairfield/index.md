---
type: Jurisdiction
title: "Fairfield County, OH"
classification: county
fips: "39045"
state: "OH"
demographics:
  population: 163453
  population_under_18: 38976
  population_18_64: 97312
  population_65_plus: 27165
  median_household_income: 90966
  poverty_rate: 8.01
  homeownership_rate: 74.92
  unemployment_rate: 3.84
  median_home_value: 298800
  gini_index: 0.416
  vacancy_rate: 5.75
  race_white: 133228
  race_black: 15064
  race_asian: 4961
  race_native: 255
  hispanic: 4508
  bachelors_plus: 48920
districts:
  - to: "us/states/oh/districts/12"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/oh/districts/senate/20"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/house/69"
    rel: in-district
    area_weight: 0.5492
  - to: "us/states/oh/districts/house/73"
    rel: in-district
    area_weight: 0.4505
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Fairfield County, OH

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 163453 |
| Under 18 | 38976 |
| 18–64 | 97312 |
| 65+ | 27165 |
| Median household income | 90966 |
| Poverty rate | 8.01 |
| Homeownership rate | 74.92 |
| Unemployment rate | 3.84 |
| Median home value | 298800 |
| Gini index | 0.416 |
| Vacancy rate | 5.75 |
| White | 133228 |
| Black | 15064 |
| Asian | 4961 |
| Native | 255 |
| Hispanic/Latino | 4508 |
| Bachelor's or higher | 48920 |

## Districts

- [OH-12](/us/states/oh/districts/12.md) — 100% (congressional)
- [OH Senate District 20](/us/states/oh/districts/senate/20.md) — 100% (state senate)
- [OH House District 69](/us/states/oh/districts/house/69.md) — 55% (state house)
- [OH House District 73](/us/states/oh/districts/house/73.md) — 45% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
