---
type: Jurisdiction
title: "Sumner County, TN"
classification: county
fips: "47165"
state: "TN"
demographics:
  population: 204424
  population_under_18: 47217
  population_18_64: 123176
  population_65_plus: 34031
  median_household_income: 90301
  poverty_rate: 8.82
  homeownership_rate: 71.96
  unemployment_rate: 3.56
  median_home_value: 393100
  gini_index: 0.4331
  vacancy_rate: 5.59
  race_white: 162961
  race_black: 17412
  race_asian: 3242
  race_native: 531
  hispanic: 14779
  bachelors_plus: 64172
districts:
  - to: "us/states/tn/districts/06"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/tn/districts/senate/18"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/tn/districts/house/44"
    rel: in-district
    area_weight: 0.5931
  - to: "us/states/tn/districts/house/35"
    rel: in-district
    area_weight: 0.2206
  - to: "us/states/tn/districts/house/45"
    rel: in-district
    area_weight: 0.1841
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Sumner County, TN

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 204424 |
| Under 18 | 47217 |
| 18–64 | 123176 |
| 65+ | 34031 |
| Median household income | 90301 |
| Poverty rate | 8.82 |
| Homeownership rate | 71.96 |
| Unemployment rate | 3.56 |
| Median home value | 393100 |
| Gini index | 0.4331 |
| Vacancy rate | 5.59 |
| White | 162961 |
| Black | 17412 |
| Asian | 3242 |
| Native | 531 |
| Hispanic/Latino | 14779 |
| Bachelor's or higher | 64172 |

## Districts

- [TN-06](/us/states/tn/districts/06.md) — 100% (congressional)
- [TN Senate District 18](/us/states/tn/districts/senate/18.md) — 100% (state senate)
- [TN House District 44](/us/states/tn/districts/house/44.md) — 59% (state house)
- [TN House District 35](/us/states/tn/districts/house/35.md) — 22% (state house)
- [TN House District 45](/us/states/tn/districts/house/45.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
