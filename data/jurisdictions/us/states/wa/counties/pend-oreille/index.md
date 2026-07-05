---
type: Jurisdiction
title: "Pend Oreille County, WA"
classification: county
fips: "53051"
state: "WA"
demographics:
  population: 14050
  population_under_18: 2715
  population_18_64: 7494
  population_65_plus: 3841
  median_household_income: 67436
  poverty_rate: 14.38
  homeownership_rate: 80.82
  unemployment_rate: 6.08
  median_home_value: 367900
  gini_index: 0.445
  vacancy_rate: 26.67
  race_white: 12038
  race_black: 25
  race_asian: 71
  race_native: 299
  hispanic: 565
  bachelors_plus: 2980
districts:
  - to: "us/states/wa/districts/05"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wa/districts/senate/7"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wa/districts/house/7"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Pend Oreille County, WA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14050 |
| Under 18 | 2715 |
| 18–64 | 7494 |
| 65+ | 3841 |
| Median household income | 67436 |
| Poverty rate | 14.38 |
| Homeownership rate | 80.82 |
| Unemployment rate | 6.08 |
| Median home value | 367900 |
| Gini index | 0.445 |
| Vacancy rate | 26.67 |
| White | 12038 |
| Black | 25 |
| Asian | 71 |
| Native | 299 |
| Hispanic/Latino | 565 |
| Bachelor's or higher | 2980 |

## Districts

- [WA-05](/us/states/wa/districts/05.md) — 100% (congressional)
- [WA Senate District 7](/us/states/wa/districts/senate/7.md) — 100% (state senate)
- [WA House District 7](/us/states/wa/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
