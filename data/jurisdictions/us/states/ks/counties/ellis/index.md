---
type: Jurisdiction
title: "Ellis County, KS"
classification: county
fips: "20051"
state: "KS"
demographics:
  population: 28920
  population_under_18: 5820
  population_18_64: 18484
  population_65_plus: 4616
  median_household_income: 63084
  poverty_rate: 18.35
  homeownership_rate: 63.19
  unemployment_rate: 3.25
  median_home_value: 216300
  gini_index: 0.489
  vacancy_rate: 7.8
  race_white: 25650
  race_black: 533
  race_asian: 452
  race_native: 61
  hispanic: 2110
  bachelors_plus: 9256
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/40"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/110"
    rel: in-district
    area_weight: 0.926
  - to: "us/states/ks/districts/house/111"
    rel: in-district
    area_weight: 0.0739
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Ellis County, KS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28920 |
| Under 18 | 5820 |
| 18–64 | 18484 |
| 65+ | 4616 |
| Median household income | 63084 |
| Poverty rate | 18.35 |
| Homeownership rate | 63.19 |
| Unemployment rate | 3.25 |
| Median home value | 216300 |
| Gini index | 0.489 |
| Vacancy rate | 7.8 |
| White | 25650 |
| Black | 533 |
| Asian | 452 |
| Native | 61 |
| Hispanic/Latino | 2110 |
| Bachelor's or higher | 9256 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 40](/us/states/ks/districts/senate/40.md) — 100% (state senate)
- [KS House District 110](/us/states/ks/districts/house/110.md) — 93% (state house)
- [KS House District 111](/us/states/ks/districts/house/111.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
