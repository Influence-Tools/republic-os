---
type: Jurisdiction
title: "Klickitat County, WA"
classification: county
fips: "53039"
state: "WA"
demographics:
  population: 23411
  population_under_18: 4250
  population_18_64: 13283
  population_65_plus: 5878
  median_household_income: 71042
  poverty_rate: 12.93
  homeownership_rate: 76.67
  unemployment_rate: 5.22
  median_home_value: 425300
  gini_index: 0.4533
  vacancy_rate: 9.8
  race_white: 19171
  race_black: 81
  race_asian: 179
  race_native: 331
  hispanic: 3089
  bachelors_plus: 7995
districts:
  - to: "us/states/wa/districts/04"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wa/districts/senate/14"
    rel: in-district
    area_weight: 0.671
  - to: "us/states/wa/districts/senate/17"
    rel: in-district
    area_weight: 0.3289
  - to: "us/states/wa/districts/house/14"
    rel: in-district
    area_weight: 0.671
  - to: "us/states/wa/districts/house/17"
    rel: in-district
    area_weight: 0.3289
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Klickitat County, WA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23411 |
| Under 18 | 4250 |
| 18–64 | 13283 |
| 65+ | 5878 |
| Median household income | 71042 |
| Poverty rate | 12.93 |
| Homeownership rate | 76.67 |
| Unemployment rate | 5.22 |
| Median home value | 425300 |
| Gini index | 0.4533 |
| Vacancy rate | 9.8 |
| White | 19171 |
| Black | 81 |
| Asian | 179 |
| Native | 331 |
| Hispanic/Latino | 3089 |
| Bachelor's or higher | 7995 |

## Districts

- [WA-04](/us/states/wa/districts/04.md) — 100% (congressional)
- [WA Senate District 14](/us/states/wa/districts/senate/14.md) — 67% (state senate)
- [WA Senate District 17](/us/states/wa/districts/senate/17.md) — 33% (state senate)
- [WA House District 14](/us/states/wa/districts/house/14.md) — 67% (state house)
- [WA House District 17](/us/states/wa/districts/house/17.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
