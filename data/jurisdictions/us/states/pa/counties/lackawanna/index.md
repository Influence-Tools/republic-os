---
type: Jurisdiction
title: "Lackawanna County, PA"
classification: county
fips: "42069"
state: "PA"
demographics:
  population: 216146
  population_under_18: 44213
  population_18_64: 127523
  population_65_plus: 44410
  median_household_income: 66223
  poverty_rate: 14.36
  homeownership_rate: 65.42
  unemployment_rate: 4.91
  median_home_value: 201800
  gini_index: 0.4667
  vacancy_rate: 11.89
  race_white: 175665
  race_black: 6807
  race_asian: 6465
  race_native: 180
  hispanic: 21190
  bachelors_plus: 65567
districts:
  - to: "us/states/pa/districts/08"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/pa/districts/senate/40"
    rel: in-district
    area_weight: 0.537
  - to: "us/states/pa/districts/senate/22"
    rel: in-district
    area_weight: 0.4629
  - to: "us/states/pa/districts/house/113"
    rel: in-district
    area_weight: 0.3445
  - to: "us/states/pa/districts/house/112"
    rel: in-district
    area_weight: 0.2544
  - to: "us/states/pa/districts/house/114"
    rel: in-district
    area_weight: 0.2469
  - to: "us/states/pa/districts/house/118"
    rel: in-district
    area_weight: 0.1539
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Lackawanna County, PA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 216146 |
| Under 18 | 44213 |
| 18–64 | 127523 |
| 65+ | 44410 |
| Median household income | 66223 |
| Poverty rate | 14.36 |
| Homeownership rate | 65.42 |
| Unemployment rate | 4.91 |
| Median home value | 201800 |
| Gini index | 0.4667 |
| Vacancy rate | 11.89 |
| White | 175665 |
| Black | 6807 |
| Asian | 6465 |
| Native | 180 |
| Hispanic/Latino | 21190 |
| Bachelor's or higher | 65567 |

## Districts

- [PA-08](/us/states/pa/districts/08.md) — 100% (congressional)
- [PA Senate District 40](/us/states/pa/districts/senate/40.md) — 54% (state senate)
- [PA Senate District 22](/us/states/pa/districts/senate/22.md) — 46% (state senate)
- [PA House District 113](/us/states/pa/districts/house/113.md) — 34% (state house)
- [PA House District 112](/us/states/pa/districts/house/112.md) — 25% (state house)
- [PA House District 114](/us/states/pa/districts/house/114.md) — 25% (state house)
- [PA House District 118](/us/states/pa/districts/house/118.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
