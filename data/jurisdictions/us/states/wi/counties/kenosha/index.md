---
type: Jurisdiction
title: "Kenosha County, WI"
classification: county
fips: "55059"
state: "WI"
demographics:
  population: 168438
  population_under_18: 36594
  population_18_64: 105180
  population_65_plus: 26664
  median_household_income: 81239
  poverty_rate: 10.49
  homeownership_rate: 66.71
  unemployment_rate: 4.41
  median_home_value: 265500
  gini_index: 0.4279
  vacancy_rate: 6.48
  race_white: 126687
  race_black: 10300
  race_asian: 3108
  race_native: 663
  hispanic: 25582
  bachelors_plus: 48439
districts:
  - to: "us/states/wi/districts/01"
    rel: in-district
    area_weight: 0.369
  - to: "us/states/wi/districts/senate/11"
    rel: in-district
    area_weight: 0.2817
  - to: "us/states/wi/districts/senate/22"
    rel: in-district
    area_weight: 0.0871
  - to: "us/states/wi/districts/house/32"
    rel: in-district
    area_weight: 0.2817
  - to: "us/states/wi/districts/house/64"
    rel: in-district
    area_weight: 0.0596
  - to: "us/states/wi/districts/house/65"
    rel: in-district
    area_weight: 0.0275
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Kenosha County, WI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 168438 |
| Under 18 | 36594 |
| 18–64 | 105180 |
| 65+ | 26664 |
| Median household income | 81239 |
| Poverty rate | 10.49 |
| Homeownership rate | 66.71 |
| Unemployment rate | 4.41 |
| Median home value | 265500 |
| Gini index | 0.4279 |
| Vacancy rate | 6.48 |
| White | 126687 |
| Black | 10300 |
| Asian | 3108 |
| Native | 663 |
| Hispanic/Latino | 25582 |
| Bachelor's or higher | 48439 |

## Districts

- [WI-01](/us/states/wi/districts/01.md) — 37% (congressional)
- [WI Senate District 11](/us/states/wi/districts/senate/11.md) — 28% (state senate)
- [WI Senate District 22](/us/states/wi/districts/senate/22.md) — 9% (state senate)
- [WI House District 32](/us/states/wi/districts/house/32.md) — 28% (state house)
- [WI House District 64](/us/states/wi/districts/house/64.md) — 6% (state house)
- [WI House District 65](/us/states/wi/districts/house/65.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
