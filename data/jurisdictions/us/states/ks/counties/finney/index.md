---
type: Jurisdiction
title: "Finney County, KS"
classification: county
fips: "20055"
state: "KS"
demographics:
  population: 38084
  population_under_18: 11379
  population_18_64: 22180
  population_65_plus: 4525
  median_household_income: 73009
  poverty_rate: 11.08
  homeownership_rate: 64.93
  unemployment_rate: 4.06
  median_home_value: 201400
  gini_index: 0.3922
  vacancy_rate: 7.84
  race_white: 19095
  race_black: 1752
  race_asian: 1471
  race_native: 232
  hispanic: 20246
  bachelors_plus: 5671
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/39"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/122"
    rel: in-district
    area_weight: 0.9932
  - to: "us/states/ks/districts/house/123"
    rel: in-district
    area_weight: 0.0068
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Finney County, KS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 38084 |
| Under 18 | 11379 |
| 18–64 | 22180 |
| 65+ | 4525 |
| Median household income | 73009 |
| Poverty rate | 11.08 |
| Homeownership rate | 64.93 |
| Unemployment rate | 4.06 |
| Median home value | 201400 |
| Gini index | 0.3922 |
| Vacancy rate | 7.84 |
| White | 19095 |
| Black | 1752 |
| Asian | 1471 |
| Native | 232 |
| Hispanic/Latino | 20246 |
| Bachelor's or higher | 5671 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 39](/us/states/ks/districts/senate/39.md) — 100% (state senate)
- [KS House District 122](/us/states/ks/districts/house/122.md) — 99% (state house)
- [KS House District 123](/us/states/ks/districts/house/123.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
