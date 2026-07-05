---
type: Jurisdiction
title: "Rockland County, NY"
classification: county
fips: "36087"
state: "NY"
demographics:
  population: 341883
  population_under_18: 101629
  population_18_64: 186585
  population_65_plus: 53669
  median_household_income: 109959
  poverty_rate: 16.25
  homeownership_rate: 67.93
  unemployment_rate: 5.6
  median_home_value: 596900
  gini_index: 0.4706
  vacancy_rate: 4.65
  race_white: 213256
  race_black: 36482
  race_asian: 20530
  race_native: 1457
  hispanic: 70586
  bachelors_plus: 129326
districts:
  - to: "us/states/ny/districts/17"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/senate/38"
    rel: in-district
    area_weight: 0.8409
  - to: "us/states/ny/districts/senate/40"
    rel: in-district
    area_weight: 0.159
  - to: "us/states/ny/districts/house/96"
    rel: in-district
    area_weight: 0.39
  - to: "us/states/ny/districts/house/97"
    rel: in-district
    area_weight: 0.2268
  - to: "us/states/ny/districts/house/98"
    rel: in-district
    area_weight: 0.2241
  - to: "us/states/ny/districts/house/99"
    rel: in-district
    area_weight: 0.159
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Rockland County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 341883 |
| Under 18 | 101629 |
| 18–64 | 186585 |
| 65+ | 53669 |
| Median household income | 109959 |
| Poverty rate | 16.25 |
| Homeownership rate | 67.93 |
| Unemployment rate | 5.6 |
| Median home value | 596900 |
| Gini index | 0.4706 |
| Vacancy rate | 4.65 |
| White | 213256 |
| Black | 36482 |
| Asian | 20530 |
| Native | 1457 |
| Hispanic/Latino | 70586 |
| Bachelor's or higher | 129326 |

## Districts

- [NY-17](/us/states/ny/districts/17.md) — 100% (congressional)
- [NY Senate District 38](/us/states/ny/districts/senate/38.md) — 84% (state senate)
- [NY Senate District 40](/us/states/ny/districts/senate/40.md) — 16% (state senate)
- [NY House District 96](/us/states/ny/districts/house/96.md) — 39% (state house)
- [NY House District 97](/us/states/ny/districts/house/97.md) — 23% (state house)
- [NY House District 98](/us/states/ny/districts/house/98.md) — 22% (state house)
- [NY House District 99](/us/states/ny/districts/house/99.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
