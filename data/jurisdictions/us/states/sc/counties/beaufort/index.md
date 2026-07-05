---
type: Jurisdiction
title: "Beaufort County, SC"
classification: county
fips: "45013"
state: "SC"
demographics:
  population: 195289
  population_under_18: 34071
  population_18_64: 105785
  population_65_plus: 55433
  median_household_income: 86573
  poverty_rate: 9.63
  homeownership_rate: 75.94
  unemployment_rate: 2.62
  median_home_value: 455600
  gini_index: 0.4803
  vacancy_rate: 20.2
  race_white: 135185
  race_black: 30745
  race_asian: 2314
  race_native: 501
  hispanic: 24168
  bachelors_plus: 92777
districts:
  - to: "us/states/sc/districts/01"
    rel: in-district
    area_weight: 0.7601
  - to: "us/states/sc/districts/senate/43"
    rel: in-district
    area_weight: 0.2974
  - to: "us/states/sc/districts/senate/46"
    rel: in-district
    area_weight: 0.2341
  - to: "us/states/sc/districts/senate/45"
    rel: in-district
    area_weight: 0.2338
  - to: "us/states/sc/districts/house/121"
    rel: in-district
    area_weight: 0.3386
  - to: "us/states/sc/districts/house/120"
    rel: in-district
    area_weight: 0.184
  - to: "us/states/sc/districts/house/124"
    rel: in-district
    area_weight: 0.1255
  - to: "us/states/sc/districts/house/123"
    rel: in-district
    area_weight: 0.0662
  - to: "us/states/sc/districts/house/118"
    rel: in-district
    area_weight: 0.0491
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Beaufort County, SC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 195289 |
| Under 18 | 34071 |
| 18–64 | 105785 |
| 65+ | 55433 |
| Median household income | 86573 |
| Poverty rate | 9.63 |
| Homeownership rate | 75.94 |
| Unemployment rate | 2.62 |
| Median home value | 455600 |
| Gini index | 0.4803 |
| Vacancy rate | 20.2 |
| White | 135185 |
| Black | 30745 |
| Asian | 2314 |
| Native | 501 |
| Hispanic/Latino | 24168 |
| Bachelor's or higher | 92777 |

## Districts

- [SC-01](/us/states/sc/districts/01.md) — 76% (congressional)
- [SC Senate District 43](/us/states/sc/districts/senate/43.md) — 30% (state senate)
- [SC Senate District 46](/us/states/sc/districts/senate/46.md) — 23% (state senate)
- [SC Senate District 45](/us/states/sc/districts/senate/45.md) — 23% (state senate)
- [SC House District 121](/us/states/sc/districts/house/121.md) — 34% (state house)
- [SC House District 120](/us/states/sc/districts/house/120.md) — 18% (state house)
- [SC House District 124](/us/states/sc/districts/house/124.md) — 13% (state house)
- [SC House District 123](/us/states/sc/districts/house/123.md) — 7% (state house)
- [SC House District 118](/us/states/sc/districts/house/118.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
