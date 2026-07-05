---
type: Jurisdiction
title: "Barrow County, GA"
classification: county
fips: "13013"
state: "GA"
demographics:
  population: 89886
  population_under_18: 22595
  population_18_64: 55717
  population_65_plus: 11574
  median_household_income: 80653
  poverty_rate: 9.55
  homeownership_rate: 78.5
  unemployment_rate: 3.75
  median_home_value: 294700
  gini_index: 0.385
  vacancy_rate: 4.52
  race_white: 59843
  race_black: 12551
  race_asian: 3627
  race_native: 514
  hispanic: 13741
  bachelors_plus: 17136
districts:
  - to: "us/states/ga/districts/10"
    rel: in-district
    area_weight: 0.9942
  - to: "us/states/ga/districts/09"
    rel: in-district
    area_weight: 0.0058
  - to: "us/states/ga/districts/senate/47"
    rel: in-district
    area_weight: 0.4514
  - to: "us/states/ga/districts/senate/45"
    rel: in-district
    area_weight: 0.3941
  - to: "us/states/ga/districts/senate/46"
    rel: in-district
    area_weight: 0.1545
  - to: "us/states/ga/districts/house/119"
    rel: in-district
    area_weight: 0.655
  - to: "us/states/ga/districts/house/104"
    rel: in-district
    area_weight: 0.2569
  - to: "us/states/ga/districts/house/120"
    rel: in-district
    area_weight: 0.0872
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Barrow County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 89886 |
| Under 18 | 22595 |
| 18–64 | 55717 |
| 65+ | 11574 |
| Median household income | 80653 |
| Poverty rate | 9.55 |
| Homeownership rate | 78.5 |
| Unemployment rate | 3.75 |
| Median home value | 294700 |
| Gini index | 0.385 |
| Vacancy rate | 4.52 |
| White | 59843 |
| Black | 12551 |
| Asian | 3627 |
| Native | 514 |
| Hispanic/Latino | 13741 |
| Bachelor's or higher | 17136 |

## Districts

- [GA-10](/us/states/ga/districts/10.md) — 99% (congressional)
- [GA-09](/us/states/ga/districts/09.md) — 1% (congressional)
- [GA Senate District 47](/us/states/ga/districts/senate/47.md) — 45% (state senate)
- [GA Senate District 45](/us/states/ga/districts/senate/45.md) — 39% (state senate)
- [GA Senate District 46](/us/states/ga/districts/senate/46.md) — 15% (state senate)
- [GA House District 119](/us/states/ga/districts/house/119.md) — 66% (state house)
- [GA House District 104](/us/states/ga/districts/house/104.md) — 26% (state house)
- [GA House District 120](/us/states/ga/districts/house/120.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
