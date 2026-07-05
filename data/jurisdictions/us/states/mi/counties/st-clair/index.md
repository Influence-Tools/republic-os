---
type: Jurisdiction
title: "St. Clair County, MI"
classification: county
fips: "26147"
state: "MI"
demographics:
  population: 160221
  population_under_18: 32478
  population_18_64: 95094
  population_65_plus: 32649
  median_household_income: 71270
  poverty_rate: 11.28
  homeownership_rate: 80.78
  unemployment_rate: 5.72
  median_home_value: 224600
  gini_index: 0.4284
  vacancy_rate: 6.84
  race_white: 146136
  race_black: 3491
  race_asian: 865
  race_native: 271
  hispanic: 5905
  bachelors_plus: 32145
districts:
  - to: "us/states/mi/districts/09"
    rel: in-district
    area_weight: 0.8948
  - to: "us/states/mi/districts/senate/25"
    rel: in-district
    area_weight: 0.8101
  - to: "us/states/mi/districts/senate/12"
    rel: in-district
    area_weight: 0.0824
  - to: "us/states/mi/districts/house/65"
    rel: in-district
    area_weight: 0.4588
  - to: "us/states/mi/districts/house/64"
    rel: in-district
    area_weight: 0.243
  - to: "us/states/mi/districts/house/63"
    rel: in-district
    area_weight: 0.1908
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# St. Clair County, MI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 160221 |
| Under 18 | 32478 |
| 18–64 | 95094 |
| 65+ | 32649 |
| Median household income | 71270 |
| Poverty rate | 11.28 |
| Homeownership rate | 80.78 |
| Unemployment rate | 5.72 |
| Median home value | 224600 |
| Gini index | 0.4284 |
| Vacancy rate | 6.84 |
| White | 146136 |
| Black | 3491 |
| Asian | 865 |
| Native | 271 |
| Hispanic/Latino | 5905 |
| Bachelor's or higher | 32145 |

## Districts

- [MI-09](/us/states/mi/districts/09.md) — 89% (congressional)
- [MI Senate District 25](/us/states/mi/districts/senate/25.md) — 81% (state senate)
- [MI Senate District 12](/us/states/mi/districts/senate/12.md) — 8% (state senate)
- [MI House District 65](/us/states/mi/districts/house/65.md) — 46% (state house)
- [MI House District 64](/us/states/mi/districts/house/64.md) — 24% (state house)
- [MI House District 63](/us/states/mi/districts/house/63.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
