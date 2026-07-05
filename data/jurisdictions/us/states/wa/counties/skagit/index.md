---
type: Jurisdiction
title: "Skagit County, WA"
classification: county
fips: "53057"
state: "WA"
demographics:
  population: 131328
  population_under_18: 27432
  population_18_64: 74205
  population_65_plus: 29691
  median_household_income: 89263
  poverty_rate: 11.61
  homeownership_rate: 70.06
  unemployment_rate: 4.87
  median_home_value: 545100
  gini_index: 0.4327
  vacancy_rate: 8.28
  race_white: 98556
  race_black: 1020
  race_asian: 2739
  race_native: 1862
  hispanic: 25367
  bachelors_plus: 39728
districts:
  - to: "us/states/wa/districts/02"
    rel: in-district
    area_weight: 0.9157
  - to: "us/states/wa/districts/senate/39"
    rel: in-district
    area_weight: 0.7938
  - to: "us/states/wa/districts/senate/40"
    rel: in-district
    area_weight: 0.0727
  - to: "us/states/wa/districts/senate/10"
    rel: in-district
    area_weight: 0.0493
  - to: "us/states/wa/districts/house/39"
    rel: in-district
    area_weight: 0.7938
  - to: "us/states/wa/districts/house/40"
    rel: in-district
    area_weight: 0.0727
  - to: "us/states/wa/districts/house/10"
    rel: in-district
    area_weight: 0.0493
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Skagit County, WA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 131328 |
| Under 18 | 27432 |
| 18–64 | 74205 |
| 65+ | 29691 |
| Median household income | 89263 |
| Poverty rate | 11.61 |
| Homeownership rate | 70.06 |
| Unemployment rate | 4.87 |
| Median home value | 545100 |
| Gini index | 0.4327 |
| Vacancy rate | 8.28 |
| White | 98556 |
| Black | 1020 |
| Asian | 2739 |
| Native | 1862 |
| Hispanic/Latino | 25367 |
| Bachelor's or higher | 39728 |

## Districts

- [WA-02](/us/states/wa/districts/02.md) — 92% (congressional)
- [WA Senate District 39](/us/states/wa/districts/senate/39.md) — 79% (state senate)
- [WA Senate District 40](/us/states/wa/districts/senate/40.md) — 7% (state senate)
- [WA Senate District 10](/us/states/wa/districts/senate/10.md) — 5% (state senate)
- [WA House District 39](/us/states/wa/districts/house/39.md) — 79% (state house)
- [WA House District 40](/us/states/wa/districts/house/40.md) — 7% (state house)
- [WA House District 10](/us/states/wa/districts/house/10.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
