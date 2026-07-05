---
type: Jurisdiction
title: "Geary County, KS"
classification: county
fips: "20061"
state: "KS"
demographics:
  population: 35815
  population_under_18: 11373
  population_18_64: 21333
  population_65_plus: 3109
  median_household_income: 59317
  poverty_rate: 18.01
  homeownership_rate: 43.52
  unemployment_rate: 6.93
  median_home_value: 172700
  gini_index: 0.3884
  vacancy_rate: 11.17
  race_white: 21186
  race_black: 5237
  race_asian: 1110
  race_native: 241
  hispanic: 6050
  bachelors_plus: 6801
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 0.997
  - to: "us/states/ks/districts/senate/17"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/house/68"
    rel: in-district
    area_weight: 0.7565
  - to: "us/states/ks/districts/house/65"
    rel: in-district
    area_weight: 0.2434
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Geary County, KS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 35815 |
| Under 18 | 11373 |
| 18–64 | 21333 |
| 65+ | 3109 |
| Median household income | 59317 |
| Poverty rate | 18.01 |
| Homeownership rate | 43.52 |
| Unemployment rate | 6.93 |
| Median home value | 172700 |
| Gini index | 0.3884 |
| Vacancy rate | 11.17 |
| White | 21186 |
| Black | 5237 |
| Asian | 1110 |
| Native | 241 |
| Hispanic/Latino | 6050 |
| Bachelor's or higher | 6801 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 17](/us/states/ks/districts/senate/17.md) — 100% (state senate)
- [KS House District 68](/us/states/ks/districts/house/68.md) — 76% (state house)
- [KS House District 65](/us/states/ks/districts/house/65.md) — 24% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
