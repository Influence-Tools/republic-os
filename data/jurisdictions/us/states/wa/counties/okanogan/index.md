---
type: Jurisdiction
title: "Okanogan County, WA"
classification: county
fips: "53047"
state: "WA"
demographics:
  population: 43425
  population_under_18: 9387
  population_18_64: 23964
  population_65_plus: 10074
  median_household_income: 63207
  poverty_rate: 20.74
  homeownership_rate: 72.39
  unemployment_rate: 4.52
  median_home_value: 299800
  gini_index: 0.4592
  vacancy_rate: 20.83
  race_white: 27935
  race_black: 559
  race_asian: 303
  race_native: 3847
  hispanic: 9128
  bachelors_plus: 10737
districts:
  - to: "us/states/wa/districts/04"
    rel: in-district
    area_weight: 0.9993
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

# Okanogan County, WA

County jurisdiction — 6 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43425 |
| Under 18 | 9387 |
| 18–64 | 23964 |
| 65+ | 10074 |
| Median household income | 63207 |
| Poverty rate | 20.74 |
| Homeownership rate | 72.39 |
| Unemployment rate | 4.52 |
| Median home value | 299800 |
| Gini index | 0.4592 |
| Vacancy rate | 20.83 |
| White | 27935 |
| Black | 559 |
| Asian | 303 |
| Native | 3847 |
| Hispanic/Latino | 9128 |
| Bachelor's or higher | 10737 |

## Districts

- [WA-04](/us/states/wa/districts/04.md) — 100% (congressional)
- [WA Senate District 7](/us/states/wa/districts/senate/7.md) — 100% (state senate)
- [WA House District 7](/us/states/wa/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
