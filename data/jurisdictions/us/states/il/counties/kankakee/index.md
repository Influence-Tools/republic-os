---
type: Jurisdiction
title: "Kankakee County, IL"
classification: county
fips: "17091"
state: "IL"
demographics:
  population: 106635
  population_under_18: 24272
  population_18_64: 63333
  population_65_plus: 19030
  median_household_income: 71281
  poverty_rate: 12.2
  homeownership_rate: 69.86
  unemployment_rate: 4.94
  median_home_value: 192600
  gini_index: 0.4433
  vacancy_rate: 9.73
  race_white: 78270
  race_black: 15265
  race_asian: 1067
  race_native: 487
  hispanic: 13523
  bachelors_plus: 21067
districts:
  - to: "us/states/il/districts/02"
    rel: in-district
    area_weight: 0.8582
  - to: "us/states/il/districts/01"
    rel: in-district
    area_weight: 0.1416
  - to: "us/states/il/districts/senate/40"
    rel: in-district
    area_weight: 0.5184
  - to: "us/states/il/districts/senate/17"
    rel: in-district
    area_weight: 0.3314
  - to: "us/states/il/districts/senate/15"
    rel: in-district
    area_weight: 0.15
  - to: "us/states/il/districts/house/79"
    rel: in-district
    area_weight: 0.5184
  - to: "us/states/il/districts/house/34"
    rel: in-district
    area_weight: 0.3314
  - to: "us/states/il/districts/house/29"
    rel: in-district
    area_weight: 0.15
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Kankakee County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 106635 |
| Under 18 | 24272 |
| 18–64 | 63333 |
| 65+ | 19030 |
| Median household income | 71281 |
| Poverty rate | 12.2 |
| Homeownership rate | 69.86 |
| Unemployment rate | 4.94 |
| Median home value | 192600 |
| Gini index | 0.4433 |
| Vacancy rate | 9.73 |
| White | 78270 |
| Black | 15265 |
| Asian | 1067 |
| Native | 487 |
| Hispanic/Latino | 13523 |
| Bachelor's or higher | 21067 |

## Districts

- [IL-02](/us/states/il/districts/02.md) — 86% (congressional)
- [IL-01](/us/states/il/districts/01.md) — 14% (congressional)
- [IL Senate District 40](/us/states/il/districts/senate/40.md) — 52% (state senate)
- [IL Senate District 17](/us/states/il/districts/senate/17.md) — 33% (state senate)
- [IL Senate District 15](/us/states/il/districts/senate/15.md) — 15% (state senate)
- [IL House District 79](/us/states/il/districts/house/79.md) — 52% (state house)
- [IL House District 34](/us/states/il/districts/house/34.md) — 33% (state house)
- [IL House District 29](/us/states/il/districts/house/29.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
