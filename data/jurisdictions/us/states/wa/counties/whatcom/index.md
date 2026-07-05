---
type: Jurisdiction
title: "Whatcom County, WA"
classification: county
fips: "53073"
state: "WA"
demographics:
  population: 230503
  population_under_18: 42743
  population_18_64: 144192
  population_65_plus: 43568
  median_household_income: 81784
  poverty_rate: 12.88
  homeownership_rate: 63.71
  unemployment_rate: 4.78
  median_home_value: 585800
  gini_index: 0.4618
  vacancy_rate: 9.18
  race_white: 179852
  race_black: 2213
  race_asian: 10078
  race_native: 4102
  hispanic: 24461
  bachelors_plus: 85596
districts:
  - to: "us/states/wa/districts/02"
    rel: in-district
    area_weight: 0.866
  - to: "us/states/wa/districts/senate/42"
    rel: in-district
    area_weight: 0.8225
  - to: "us/states/wa/districts/senate/40"
    rel: in-district
    area_weight: 0.0426
  - to: "us/states/wa/districts/house/42"
    rel: in-district
    area_weight: 0.8225
  - to: "us/states/wa/districts/house/40"
    rel: in-district
    area_weight: 0.0426
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Whatcom County, WA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 230503 |
| Under 18 | 42743 |
| 18–64 | 144192 |
| 65+ | 43568 |
| Median household income | 81784 |
| Poverty rate | 12.88 |
| Homeownership rate | 63.71 |
| Unemployment rate | 4.78 |
| Median home value | 585800 |
| Gini index | 0.4618 |
| Vacancy rate | 9.18 |
| White | 179852 |
| Black | 2213 |
| Asian | 10078 |
| Native | 4102 |
| Hispanic/Latino | 24461 |
| Bachelor's or higher | 85596 |

## Districts

- [WA-02](/us/states/wa/districts/02.md) — 87% (congressional)
- [WA Senate District 42](/us/states/wa/districts/senate/42.md) — 82% (state senate)
- [WA Senate District 40](/us/states/wa/districts/senate/40.md) — 4% (state senate)
- [WA House District 42](/us/states/wa/districts/house/42.md) — 82% (state house)
- [WA House District 40](/us/states/wa/districts/house/40.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
