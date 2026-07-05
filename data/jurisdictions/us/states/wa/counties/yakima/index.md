---
type: Jurisdiction
title: "Yakima County, WA"
classification: county
fips: "53077"
state: "WA"
demographics:
  population: 257152
  population_under_18: 74398
  population_18_64: 145487
  population_65_plus: 37267
  median_household_income: 70656
  poverty_rate: 15.46
  homeownership_rate: 61.85
  unemployment_rate: 7.33
  median_home_value: 310100
  gini_index: 0.4246
  vacancy_rate: 5.11
  race_white: 120276
  race_black: 1804
  race_asian: 3182
  race_native: 8138
  hispanic: 134645
  bachelors_plus: 41240
districts:
  - to: "us/states/wa/districts/04"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/wa/districts/senate/14"
    rel: in-district
    area_weight: 0.512
  - to: "us/states/wa/districts/senate/15"
    rel: in-district
    area_weight: 0.4879
  - to: "us/states/wa/districts/house/14"
    rel: in-district
    area_weight: 0.512
  - to: "us/states/wa/districts/house/15"
    rel: in-district
    area_weight: 0.4879
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Yakima County, WA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 257152 |
| Under 18 | 74398 |
| 18–64 | 145487 |
| 65+ | 37267 |
| Median household income | 70656 |
| Poverty rate | 15.46 |
| Homeownership rate | 61.85 |
| Unemployment rate | 7.33 |
| Median home value | 310100 |
| Gini index | 0.4246 |
| Vacancy rate | 5.11 |
| White | 120276 |
| Black | 1804 |
| Asian | 3182 |
| Native | 8138 |
| Hispanic/Latino | 134645 |
| Bachelor's or higher | 41240 |

## Districts

- [WA-04](/us/states/wa/districts/04.md) — 100% (congressional)
- [WA Senate District 14](/us/states/wa/districts/senate/14.md) — 51% (state senate)
- [WA Senate District 15](/us/states/wa/districts/senate/15.md) — 49% (state senate)
- [WA House District 14](/us/states/wa/districts/house/14.md) — 51% (state house)
- [WA House District 15](/us/states/wa/districts/house/15.md) — 49% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
